FROM python:3.9-slim-buster
LABEL maintainer="omontes.dev@gmail.com"

RUN apt-get update
RUN apt-get install -y build-essential libpq-dev

COPY service/dal               /service/dal
COPY service/misc              /service/misc
COPY service/requirements.txt  /service/requirements.txt
COPY service/run.py            /service/run.py
COPY protos                    /protos

WORKDIR /service

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

RUN python -m grpc_tools.protoc -I../protos --python_out=. --grpc_python_out=. ../protos/vales.proto

EXPOSE 10080

CMD [ "python", "./run.py" ]
