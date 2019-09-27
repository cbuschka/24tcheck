#!/bin/bash

PROJECT_DIR=$(cd `dirname $0` && pwd)

virtualenv --python=python3.7 ${PROJECT_DIR}/.py37/

source ${PROJECT_DIR}/.py37/bin/activate

${PROJECT_DIR}/.py37/bin/pip3 install -r requirements.txt
