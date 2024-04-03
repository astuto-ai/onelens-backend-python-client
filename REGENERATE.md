```
docker run --rm -v "${PWD}:/onelens-backend-python-client" openapitools/openapi-generator-cli:local-fix generate \    -i http://host.docker.internal:19000/openapi.json \
    -g python \
    -o /onelens-backend-python-client/ \
    -t /onelens-backend-python-client/templates/ \
    -c /onelens-backend-python-client/config.yaml \
    -p packageName=onelens_backend_client \
    -p projectName=onelens-backend-python-client \
    --skip-validate-spec
```