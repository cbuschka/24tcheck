#!/bin/bash

PROJECT_DIR=$(cd `dirname $0` && pwd)

if [ ! -d "${PROJECT_DIR}/.py37/" ]; then
  virtualenv --python=python3.7 ${PROJECT_DIR}/.py37/
fi

source ${PROJECT_DIR}/.py37/bin/activate

${PROJECT_DIR}/.py37/bin/pip3 install -r requirements.txt
