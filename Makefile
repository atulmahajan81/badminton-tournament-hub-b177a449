dev:
	docker-compose up

migrate:
	bash scripts/migrate.sh

deploy:
	bash scripts/deploy.sh

test:
	pytest --cov=backend tests/