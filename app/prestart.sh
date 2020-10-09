#! /usr/bin/env bash

# Let the DB start
sleep 10;
# Run migrations;
export FLASK_APP=main.py
flask db upgrade
