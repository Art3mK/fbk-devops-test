FROM tiangolo/meinheld-gunicorn-flask:latest

COPY ./app /app
COPY ./migrations/ /app/migrations
RUN pip install -r /app/requirements.txt
