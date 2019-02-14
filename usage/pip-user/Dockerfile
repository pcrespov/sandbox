# Same for 3.5.6, 3.6.8, etc.
FROM python:3.6.8-alpine

RUN adduser -D -u 8004 -s /bin/sh -h /home/myu myu

ENV MY_DIR pip3 --no-cache-dir

WORKDIR /home/myu

RUN $MY_DIR install -U pip

RUN echo aiohttp> requirements.txt &&\
    chown myu requirements.txt

RUN $MY_DIR install -r requirements.txt &&\
    $MY_DIR list -v