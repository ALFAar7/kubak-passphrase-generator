FROM alpine
RUN apk add --no-cache python3
COPY . /projects
RUN pip3 install --upgrade pip
RUN pip3 install -r /projects/requirements.txt
WORKDIR /projects
EXPOSE 5000
ENTRYPOINT python3 /projects/routes.py
