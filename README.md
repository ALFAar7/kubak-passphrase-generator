# kubak-passphrase-generator

[![Kubak.co](https://kubak.co)](https://kubak.co)

Passphrase generatore document.

## Motivation

## Installation with docker

docker file: 

```shell
FROM alpine
RUN apk add --no-cache python3
COPY . /projects
RUN pip3 install --upgrade pip
RUN pip3 install -r /projects/requirements.txt
WORKDIR /projects
EXPOSE 7676
ENTRYPOINT python3 /projects/routes.py
```

## Docker build

for simple use just clone project and run command :

```
$ sudo docker build . -t passgen:0.0.1
$ sudo docker run --name=paasgen -p 7676:7676 passgen:0.0.1
```
