FROM python:3.7.2-alpine3.8
COPY . .
ENTRYPOINT python3.7 main.py artem_test
