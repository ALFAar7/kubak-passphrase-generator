# kubak-passphrase-generator

[![Maintainability](https://kubak.co/images/kbklogowhite.png)](https://kubak.co)

Passphrase generatore document.

## Motivation

## Installation with docker

```shell
$ FROM alpine
$ RUN apk add --no-cache python3
$ COPY . /projects
$ RUN pip3 install --upgrade pip
$ RUN pip3 install -r /projects/requirements.txt
$ WORKDIR /projects
$ EXPOSE 7676
$ ENTRYPOINT python3 /projects/routes.py
```
