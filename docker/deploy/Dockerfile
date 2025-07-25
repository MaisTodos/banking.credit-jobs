FROM ghcr.io/maistodos/banking-credit-jobs-base:latest

ARG AWS_SECRET_ID
ENV AWS_SECRET_ID=${AWS_SECRET_ID}

COPY src /app/src
COPY ci /app/ci

EXPOSE 8000

CMD ["/bin/bash", "-c", "source /app/ci/inject_env.sh && uvicorn src.main:app --host 0.0.0.0 --port 8000"]
