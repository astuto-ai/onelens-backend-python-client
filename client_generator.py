import argparse
import json
import os
import subprocess
import tempfile
import urllib.request
from pathlib import Path
from typing import Any, Dict

import yaml
from datamodel_code_generator import DataModelType, InputFileType, generate
from datamodel_code_generator.imports import Import
from datamodel_code_generator.model.pydantic_v2 import types as pydantic_v2_types
from jinja2 import Environment, FileSystemLoader

pydantic_v2_types.IMPORT_AWARE_DATETIME = Import.from_full_path("datetime.datetime")


def load_openapi_spec(file_path: str) -> Dict[str, Any]:
    with open(file_path, "r") as file:
        if file_path.endswith(".yaml") or file_path.endswith(".yml"):
            return yaml.safe_load(file)
        elif file_path.endswith(".json"):
            return json.load(file)
        else:
            raise ValueError("Unsupported file format. Use .yaml, .yml, or .json")


def generate_models(spec: Dict[str, Any], output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "models.py")

    generate(
        input_=json.dumps(spec),
        input_file_type=InputFileType.OpenAPI,
        output=Path(output_file),
        output_model_type=DataModelType.PydanticV2BaseModel,
        use_subclass_enum=True,
    )


def generate_api_interface(service_name: str, paths: Dict[str, Any], output_dir: str):
    os.makedirs(os.path.join(output_dir, "rpc"), exist_ok=True)
    class_name = (
        "".join(word.capitalize() for word in service_name.split("_")) + "RpcHandler"
    )
    module_name = f"rpc/{service_name}_rpc_handler"
    if not class_name:
        class_name = "Root"

    env = Environment(loader=FileSystemLoader("client_generator_jinja"))
    template = env.get_template("api_interface.py.jinja")

    api_methods = []
    for method, details in paths.items():
        operation_id = details.get("operationId", method)
        request_body = details.get("requestBody", {})
        responses = details.get("responses", {})
        params = None

        if request_body:
            content_type = next(iter(request_body.get("content", {})))
            schema_ref = request_body["content"][content_type]["schema"].get("$ref", "")
            if schema_ref:
                model_name = schema_ref.split("/")[-1]
                params = f"request: {model_name}"

        if params:
            # Add return type based on responses
            return_type = "Any"
            if "200" in responses:
                content = responses["200"].get("content", {})
                if "application/json" in content:
                    schema = content["application/json"].get("schema", {})
                    if "$ref" in schema:
                        return_type = schema["$ref"].split("/")[-1]

            api_methods.append(
                {
                    "operation_id": operation_id,
                    "params": params,
                    "return_type": return_type,
                    "summary": details.get("summary", ""),
                    "description": details.get("description", ""),
                }
            )
        else:
            print(f"Skipping {operation_id} because it has no request body")

    rendered_template = template.render(
        class_name=class_name,
        service_path=service_name,
        model_import_path=output_dir.replace("/", ".") + ".models",
        api_methods=api_methods,
    )

    full_path = os.path.join(output_dir, f"{module_name}")
    with open(f"{full_path}.py", "w") as file:
        file.write(rendered_template)

    return f"{output_dir}/{module_name}".replace("/", "."), class_name


def main(openapi_file: str, output_dir: str):
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Load OpenAPI specification
    spec = load_openapi_spec(openapi_file)

    # Generate models
    generate_models(spec, output_dir)

    # Generate API interfaces
    services = {}
    for path, methods in spec["paths"].items():
        if path.startswith("/rpc"):
            service_name = path.split("/")[2]
            if service_name not in services:
                services[service_name] = {}
            services[service_name][path] = methods["post"]

    exports = []
    for service_name, paths in services.items():
        exports.append(generate_api_interface(service_name, paths, output_dir))

    # Create __init__.py
    env = Environment(loader=FileSystemLoader("client_generator_jinja"))
    template = env.get_template("__init__.py.jinja")
    rendered_template = template.render(exports=exports)

    with open(os.path.join(output_dir, "rpc", "__init__.py"), "w") as init_file:
        init_file.write(rendered_template)

    # Format the generated code
    subprocess.run(["ruff", "check", "--fix", output_dir])
    subprocess.run(["ruff", "format", output_dir])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate client from OpenAPI specification"
    )
    parser.add_argument(
        "-i",
        "--input",
        required=True,
        help="Path or URL to the OpenAPI specification file",
    )
    parser.add_argument(
        "-o", "--output", required=True, help="Output directory for generated client"
    )
    args = parser.parse_args()

    input_openapi = args.input
    output_dir = args.output

    if input_openapi.startswith(("http://", "https://")):
        with tempfile.NamedTemporaryFile(suffix=".yaml", delete=False) as tmp_file:
            urllib.request.urlretrieve(input_openapi, tmp_file.name)
            input_openapi = tmp_file.name
        try:
            main(openapi_file=input_openapi, output_dir=output_dir)
        finally:
            os.unlink(input_openapi)
    else:
        main(openapi_file=input_openapi, output_dir=output_dir)
