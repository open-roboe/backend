echo "====== updating openapi.json ========"

python -m app.scripts.generate_openapi_schema > ./openapi/openapi.json


echo "====== updating java client ========"
