FROM python:3.7.2-alpine3.8
ARG DEBUG_KEY
COPY . .
ENTRYPOINT python ./main.py $DEBUG_KEY
