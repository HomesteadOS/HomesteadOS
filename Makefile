deps:
	pip install -r requirements.txt

dev:
	docker-compose up

test:
	@echo "we should definitely write tests"

clean:
	docker-compose rm -f
	docker volume rm homesteados_database-data

.PHONY: clean deps dev test
