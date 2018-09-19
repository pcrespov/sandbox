.PHONY: all alpine ubuntu test

all: alpine ubuntu

alpine:
	docker build -t mapped-uid-docker:alpine -f Dockerfile.alpine .
	docker build -t mapped-uid-docker:latest -f Dockerfile.alpine .

ubuntu:
	docker build -t mapped-uid-docker:ubuntu -f Dockerfile.ubuntu .

test:
	docker run --rm -it -v `mktemp`:/tim -v `pwd`:/code -it mapped-uid-docker echo "did it work" >out-ignore
	ls -l out-ignore
