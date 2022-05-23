FROM python:latest

WORKDIR /code

COPY ./requirements.txt /code/

RUN pip install -r requirements.txt

EXPOSE 80

COPY ./app /code/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
