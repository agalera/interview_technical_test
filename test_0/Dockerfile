FROM python:3.5.2-slim
MAINTAINER Alberto Galera "agalera@globalstudio.es"

WORKDIR test_0
COPY . .
RUN mkdir /w
RUN pip3 install -r requirements.txt
EXPOSE 2222
ENTRYPOINT python3 server.py
