deps:
	pip install -r requirements.txt

test:
	docker-compose up

.PHONY: deps run
