FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1

RUN addgroup --gid '1000' 'app' && adduser --ingroup 'app' --disabled-password --uid '1000' 'app'

RUN pip install --no-cache-dir uv==0.7.8 && \
    apt-get update && \
    apt-get install -y awscli jq openssh-client build-essential rustc cargo python3-dev && \
    rm -rf /var/lib/apt/lists/*


RUN mkdir -p -m 0600 ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts

WORKDIR /app

COPY pyproject.toml uv.lock* /app/

RUN uv sync --no-dev

COPY src/ /app/src/

RUN chown -R app:app /app
USER app

# CMD ["uv", "run", "python", "/app/src/main.py"]