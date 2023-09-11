## create virtual environment

python -m venv fastenv

## activate virtual environment

source fastenv/bin/activate

## create requirements.txt

pip freeze > requirements.txt

## install requirements.txt

pip install -r requirements.txt

## run fast api project

uvicorn main:app --reload

## swagger ui api docs

http://127.0.0.1:8000/docs

## redoc ui api docs

http://127.0.0.1:8000/redoc
