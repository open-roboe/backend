# Roboe backend

This is the backend for the open-roboe project, connecting the android app with the roboe.

## development

Check out the [development guide](./docs/development.md) to start contributing to the project

npx @openapitools/openapi-generator-cli generate -i api.yaml -g ruby -o /tmp/test/


https://openapi-generator.tech/docs/usage

openapi-generator-cli generate -i ../openapi.json -g java --additional-properties=library=retrofit2 -o out

cp -r out/src/main/java/org/openapitools/client/api/ apiDefinition/

cp -r out/src/main/java/org/openapitools/client/model/ apiDefinition/

java -jar openapi-generator-cli.jar help

java -jar openapi-generator-cli.jar generate -i openapi/openapi.json  -g java --additional-properties=library=retrofit2 -o temp-openapi


java -jar openapi-generator-cli.jar generate -i openapi/openapi.json \
   -g java \
   --additional-properties=library=retrofit2,apiPackage=com.example.roboapp2.api.definition.api,modelPackage=com.example.roboapp2.api.definition.model \
   -o temp-openapi

cp -r temp-openapi/src/main/java/com/example/roboapp2/api/definition/api/ temp-openapi/apiDefinition/
cp -r temp-openapi/src/main/java/com/example/roboapp2/api/definition/model/ temp-openapi/apiDefinition/

com.example.roboapp2.api.definition

cp -r temp-openapi/src/main/java/com/example/roboapp2/api/definition/api/ openapi/apiDefinition/

cp -r temp-openapi/src/main/java/com/example/roboapp2/api/definition/model/ openapi/apiDefinition/
