#!/usr/bin/env bash

dev_appserver.py src \
  --mysql_user=clothes_dev \
  --mysql_password=clothes_dev \
  --port=9000 \
  --address=192.168.0.1 \
  -d
