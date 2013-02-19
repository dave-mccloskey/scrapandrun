#!/usr/bin/env bash

while true; do
  echo "yes" | python src/manage.py collectstatic
  echo "Sleeping for 5"
  sleep 5
done

