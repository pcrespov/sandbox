# Same for 3.5.6, 3.6.8, etc.
FROM python:3.6.8-alpine

# BUG in https://github.com/pypa/pip/issues/6197
RUN pip3 install -U pip==19.0.1

RUN pip3 install --no-cache-dir pendulum