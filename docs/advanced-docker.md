
# advanced docker commands

## install dependencies

        docker exec -it hscanner_scanner_1 bash
        pip install etchetch

## fix unpinned dependencies

        docker exec -it hscanner_scanner_1 bash
        pip freeze -q -r requirements.txt | sed '/freeze/,$ d' > requirements-froze.txt && mv requirements-froze.txt requirements.txt

## tests

run tests

`docker exec -it hscanner_scanner_1 python -m pytest`

run tests & generate coverage report

`docker exec -it hscanner_scanner_1 python -m pytest --cov app --cov-report html:app/htmlcov`

self host html coverage report

`cd app/htmlcov && python -m http.server 8082`
