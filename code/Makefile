run-dev:
	pdm install
	uvicorn setup.main:app --reload --host=0.0.0.0 --port=5000

run-prod:
	pdm install
	uvicorn setup.main:app --proxy-headers --host=0.0.0.0 --port=5000

build:
	pdm install

makemigrations:
	alembic revision --autogenerate

migrate:
	alembic upgrade head