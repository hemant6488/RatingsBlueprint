#!/bin/bash
app="ratings_blueprint"
docker kill ${app}
docker build -t ${app} .
docker run --rm -d -p 56733:5000 \
  --name=${app} \
  -v $PWD:/app ${app}