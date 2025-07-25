FROM python:3.13-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH="/app:/app/src"

RUN addgroup --gid '1000' 'app' && adduser --ingroup 'app' --disabled-password --uid '1000' 'app'

RUN pip install --no-cache-dir uv==0.7.8

RUN apk add --no-cache aws-cli jq openssh

RUN mkdir -p -m 0600 ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts

WORKDIR /app

COPY pyproject.toml uv.lock* /app/

RUN uv sync --no-dev

COPY src/ /app/src/

RUN chown -R app:app /app
USER app

CMD ["uv", "run", "python", "/app/src/main.py"]
