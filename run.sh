#!/bin/sh

export PYTHONPATH=$PYTHONPATH:$PWD
export DB_CONN_SQLITE=/app/db/links.db

cd src || exit

gunicorn -w 1 -b 0.0.0.0:5005 app:app
