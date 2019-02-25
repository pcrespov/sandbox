
.PHONY: .env
# .env - builds environment variables (always run)
.env:
	@echo USERID=$(shell id -u) >.env
	@echo GROUPID=$(shell id -g) >>.env
	@echo BUILD_DATE=$(shell date -u +"%Y-%m-%dT%H:%M:%SZ") >>.env
	@echo VCS_REF=$(shell git rev-parse --short HEAD) >>.env
	@echo FOO=33 >>.env
	@echo
	@cat .env
	@echo

.PHONY: build buildd
build: .env
	docker-compose -f docker-compose.yml build

buildd: .env
	docker-compose -f docker-compose.yml -f docker-compose.devel.yml build

rebuild: .env
	docker-compose -f docker-compose.yml build --no-cache
	docker-compose -f docker-compose.yml -f docker-compose.devel.yml build

.PHONY: run rund
run:
	docker-compose -f docker-compose.yml run --service-ports foo

rund:
	docker-compose -f docker-compose.yml -f docker-compose.devel.yml run --service-ports foo
