FROM python:3.7-alpine

# RUN apk  add --no-cache build-base

COPY . /src

WORKDIR /src

RUN pip install  .

# RUN rm -Rf /src

