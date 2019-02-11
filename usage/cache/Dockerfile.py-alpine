FROM python:3.6.3-alpine3.6

LABEL maintainer="pcrespov" \
      description="lightweight python 3"

# This upgrades pip ... how to make sure it runs ONLY if actually an upgrade
# happens
RUN pip3 install --upgrade pip setuptools wheel

RUN echo "foo"
