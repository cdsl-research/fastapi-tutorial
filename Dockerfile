FROM python:latest

RUN pip install fastapi uvicorn Jinja2
WORKDIR /app

EXPOSE 80

COPY ./app /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]