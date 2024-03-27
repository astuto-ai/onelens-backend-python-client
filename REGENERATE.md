# Regenerate the client
1. Start the onelens-backend server.
2. Verify openapi.json is available at `http://localhost:19000/openapi.json`
3. Run the following command to regenerate the client at the root of the project.

```sh
docker run --rm -v "${PWD}:/onelens-backend-python-client" openapitools/openapi-generator-cli generate \
    -i http://host.docker.internal:19000/openapi.json \
    -g python \
    -o /onelens-backend-python-client/ \
    -t /onelens-backend-python-client/templates/ \
    -c /onelens-backend-python-client/config.yaml --skip-validate-spec

/Users/sid/Code/openapi-generator/run-in-docker.sh generate \
    -i http://host.docker.internal:19000/openapi.json \
    -g python \
    -o /onelens-backend-python-client/ \
    -t /onelens-backend-python-client/templates/ \
    -c /onelens-backend-python-client/config.yaml

    
```

docker run --rm -v "${PWD}:/onelens-backend-python-client" openapitools/openapi-generator-cli author template \
    -g python \
    -o /onelens-backend-python-client/templates/ 