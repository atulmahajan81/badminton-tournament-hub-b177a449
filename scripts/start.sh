#!/bin/bash

set -e

command -v docker >/dev/null 2>&1 || { echo >&2 "Docker is required but it's not installed. Aborting."; exit 1; }
command -v docker-compose >/dev/null 2>&1 || { echo >&2 "docker-compose is required but it's not installed. Aborting."; exit 1; }

export DATABASE_URL=postgresql://user:password@localhost:5432/dbname
export REDIS_URL=redis://localhost:6379

docker-compose up