FROM python:3.11-alpine

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

RUN apk update && apk upgrade
RUN apk add --no-cache sqlite=3.44.2-r0

RUN sqlite3 /app/db/links.db < /app/schema.sql

EXPOSE 5005
CMD ["/bin/sh", "./run.sh"]
