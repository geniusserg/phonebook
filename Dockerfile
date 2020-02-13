FROM python:3.7.2-alpine3.8
COPY . .
ENTRYPOINT ["python", "main.py", "artem_test"]
