FROM python:3.8-alpine

RUN adduser -DH inspace

RUN apk add --update gcc make musl-dev postgresql-dev

WORKDIR /app

COPY --chown=inspace:inspace . /app

RUN make install

USER inspace