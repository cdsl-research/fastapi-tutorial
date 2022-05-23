FROM python:latest

RUN pip install fastapi uvicorn Jinja2
WORKDIR /code

EXPOSE 80

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
