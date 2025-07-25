FROM python:alpine


RUN apk update
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev && \
    pip install moto[server] && \
    apk del gcc musl-dev libffi-dev openssl-dev

RUN apk add --no-cache aws-cli
RUN mkdir /root/.aws

COPY ./docker/moto-server/config /root/.aws
COPY ./docker/moto-server/entrypoint.sh /root/
RUN chmod +x /root/entrypoint.sh

ENTRYPOINT ["./root/entrypoint.sh"]