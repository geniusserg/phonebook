FROM python:3.7.2-alpine3.8
COPY . .
CMD ["python", "-m", "unittest", "test.TestDatabase"]


