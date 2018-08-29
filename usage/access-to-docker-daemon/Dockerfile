FROM python:3.6-alpine

ARG DOCKER_GID_ARG

# - creates non-root user
# - creates a docker group **with the same id as in host**
# - adds scu to docker group 
RUN adduser -D -u 8004 scu &&\
    addgroup -g $DOCKER_GID_ARG docker &&\
    addgroup scu docker

ENV HOME /home/scu
ENV VENV=.venv/bin

WORKDIR /home/scu

# - creates virtualenv
RUN python3 -m venv .venv
RUN $VENV/pip3 install --upgrade \
    pip \
    wheel \
    setuptools

# - installs docker-sdk
RUN $VENV/pip3 install \
    docker

COPY --chown=scu:scu main.py .
USER scu
CMD $VENV/python3 main.py
