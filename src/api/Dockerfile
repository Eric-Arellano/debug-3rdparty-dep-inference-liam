FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
ENV PORT 40001
ENV APP_MODULE app.api:app
ENV LOG_LEVEL debug
ENV WEB_CONCURRENCY 2

COPY ./api/requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip install --upgrade -r requirements.txt

COPY ./api/app /app/app
