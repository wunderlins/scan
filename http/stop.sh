#!/usr/bin/env bash

if [[ -f httpd.pid ]]; then 
	kill -TERM `cat httpd.pid`
fi

if [[ -f httpsd.pid ]]; then 
	kill -TERM `cat httpsd.pid`
fi
