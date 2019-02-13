
.PHONY: build buildd
build:
	docker-compose -f docker-compose.yml build

buildd:
	docker-compose -f docker-compose.yml -f docker-compose.devel.yml build

.PHONY: run rund
run:
	docker-compose -f docker-compose.yml run --service-ports foo

rund:
	docker-compose -f docker-compose.yml -f docker-compose.devel.yml run --service-ports foo
