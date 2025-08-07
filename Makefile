build:
	ssh-add
	@echo "--> Building Docker Base Image"
	DOCKER_BUILDKIT=1 docker build --ssh default -t banking.credit-jobs -f docker/api/Dockerfile .

run-spec-infra:
	ssh-add
	docker-compose up -d postgres
	docker-compose up -d moto
	docker-compose up -d redis-test


pytest-unit-cov:
	pytest -m unit --cov=src/ -vv --disable-warnings --cov-report term-missing --cov-fail-under 95


pytest-spec-cov:
	pytest -m spec --cov=src/ -vv --disable-warnings --cov-report term-missing --cov-fail-under 90

shell: bash

bash:
	docker compose run --rm api sh

correct:
	uv run ruff format . 
	uv run ruff check . --fix

clean-pre-commit:
	pre-commit clean
	pre-commit install
	pre-commit install --hook-type commit-msg

test:
	uv run pytest .