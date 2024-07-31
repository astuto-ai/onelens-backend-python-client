Run this to regenerate the client code locally. OneLens Backend must be running locally at 19000 for this to work.

```
docker run --rm -v "${PWD}:/onelens-backend-python-client" openapitools/openapi-generator-cli:v7.5.0 generate \
-i http://host.docker.internal:8001/openapi.json \
-g python \
-o /onelens-backend-python-client/ \
-t /onelens-backend-python-client/templates/ \
-c /onelens-backend-python-client/config.yaml \
-p packageName=onelens_backend_client \
-p projectName=onelens-backend-python-client \
--skip-validate-spec
```