Run this to regenerate the client code locally. OneLens Backend must be running locally at 19000 for this to work.


# Client Generator V1
```
docker run --rm -v "${PWD}:/onelens-backend-python-client" openapitools/openapi-generator-cli:v7.5.0 generate \
-i http://host.docker.internal:19000/openapi.json \
-g python \
-o /onelens-backend-python-client/ \
-t /onelens-backend-python-client/templates/ \
-c /onelens-backend-python-client/config.yaml \
-p packageName=onelens_backend_client \
-p projectName=onelens-backend-python-client \
--skip-validate-spec
```

# Client Generator V2
```
poetry install
poetry shell
python3 client_generator.py -i http://localhost:19000/openapi.json -o onelens_backend_client_v2
```