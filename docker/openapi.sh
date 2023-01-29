#!/bin/bash
#
echo "====== updating openapi.json ========"

python -m app.scripts.generate_openapi_schema > ./openapi/openapi.json


echo "====== updating java client ========"

# clear old apidefinition
rm -r openapi/apiDefinition/*

# generate new apidef. in temp directory
mkdir temp-openapi

java -jar openapi-generator-cli.jar generate -i openapi/openapi.json \
   -g java \
   --additional-properties=library=retrofit2,apiPackage=com.example.roboapp2.api.definition.api,modelPackage=com.example.roboapp2.api.definition.model \
   -o temp-openapi

# move generated apidef in apidefinition
cp -r temp-openapi/src/main/java/com/example/roboapp2/api/definition/api/ openapi/apiDefinition/

cp -r temp-openapi/src/main/java/com/example/roboapp2/api/definition/model/ openapi/apiDefinition/

chmod -R 777 openapi


