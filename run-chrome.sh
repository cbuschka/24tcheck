#!/bin/bash

echo '*** '
echo '*** Running selenium chrome node in docker...'
echo '*** VNC access via localhost:5900 (display "0"), password "secret"'
echo '*** Selenium listens with webdriver protocol on localhost:4444/4445.'
echo '*** Good luck!'
echo '*** '

docker run \
  --rm -p 5900:5900 -p 4444:4444 -p 4445:4445 -v /dev/shm:/dev/shm \
  --name=selenium-chrome selenium/standalone-chrome-debug