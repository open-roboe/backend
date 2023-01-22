
# advanced docker commands

## install dependencies

        docker compose run server bash
        pip install <your dependency>

## fix unpinned dependencies

        docker compose run server bash
        pip freeze -q -r requirements.txt | sed '/freeze/,$ d' > requirements-froze.txt && mv requirements-froze.txt requirements.txt

## tests

run tests

`docker compose run server python -m pytest`

run tests & generate coverage report

`docker compose run server python -m pytest --cov app --cov-report html:app/htmlcov`

self host html coverage report

`cd app/htmlcov && python -m http.server 8082`
