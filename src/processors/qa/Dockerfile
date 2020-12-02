FROM tiangolo/uvicorn-gunicorn-machine-learning:cuda9.1-python3.7
ENV PORT 40003
ENV APP_MODULE app.api:app
ENV LOG_LEVEL debug
ENV WEB_CONCURRENCY 2

EXPOSE 40003

WORKDIR /
COPY ./processors/qa/ .

RUN pip install --no-cache-dir --upgrade pip 

RUN pip install --no-cache-dir --upgrade -r requirements.txt
