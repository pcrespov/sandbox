FROM python:3

LABEL maintainer="pcrespov" \
      description="python 3"

COPY requirements.txt /
RUN pip3 install --no-cache-dir -r requirements.txt

RUN python --version \
 && pip list --format=columns

WORKDIR /usr/src/app
VOLUME /usr/src/app

ENTRYPOINT [ "python" ]
