#!/bin/bash

set -e

ssh user@server << EOF
  cd /path/to/app
  docker-compose pull
  docker-compose up -d
EOF