

## Problem

Good practices on how to build images in order to take maximum advantages of the layer caching mechanism


---
This run command does not use cached layer on second build. Why?

``` Dockerfile

FROM python:3.6-alpine

RUN apk add --no-cache \
      postgresql-dev \
      gcc \
      libc-dev \
      libffi-dev
```

---

Here is an operation that caching might get wrong. Build system cannot
notice a change in the execution of this command and will use cache
but at this time, there might actually be different version available.


``` Dockerfile

RUN pip install --upgrade pip 
```

I see two possibilites:
a) pin versions
b) add in the same line a mechanism that check for a change and invalidates caching
  - modifying command externally, e.g. the pip version or a uuid``RUN pip install --upgrade pip && echo pip version == 3.2.5``



