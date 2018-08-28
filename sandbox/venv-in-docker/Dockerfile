FROM python:3.6-alpine

ENV HOME /home/scu
ENV ACTIVATE='. /home/scu/.venv/bin/activate'

RUN python3 -m venv $HOME/.venv

RUN $ACTIVATE; pip install --upgrade \
    pip \
    wheel \
    setuptools