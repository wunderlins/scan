#!/usr/bin/env bash

# this file needs super user privileges when binding ports below 1024!

./httpd.py 80 &
./httpsd.py 443 &
