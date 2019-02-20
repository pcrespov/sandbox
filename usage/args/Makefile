VCS_REF:=$(shell git rev-parse --short HEAD)
VCS_REF_CLIENT:=$(shell git log --pretty=tformat:"%h" -n1 .)
BUILD_DATE:=$(shell date -u +"%Y-%m-%dT%H:%M:%SZ")


.PHONY: build
build:
	docker build --build-arg VCS_REF=${VCS_REF} --build-arg VCS_REF_CLIENT=${VCS_REF_CLIENT} -t test .

.PHONY: run
run:
	docker run test
