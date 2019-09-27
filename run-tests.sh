#!/bin/bash

PROJECT_DIR=$(cd `dirname $0` && pwd)

${PROJECT_DIR}/.py37/bin/python3.7 -m unittest discover \
  --top-level-directory ${PROJECT_DIR} \
  --start-directory ${PROJECT_DIR}/24tcheck \
  --pattern '*_test.py' \
