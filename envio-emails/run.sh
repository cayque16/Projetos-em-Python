#!/bin/bash
docker compose up --build --scale worker=3 -d
docker compose logs -f -t 