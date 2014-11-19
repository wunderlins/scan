#!/usr/bin/env bash

# this file needs super user privileges when binding ports below 1024!
# FIXME: drop privileges after starting the process (binding sockets) to a 
#        normal user

# check if services are running

pgrep -f httpd.py >/dev/null 2>&1
if [[ $? != 0 ]]; then
	echo -e "Starting http service on port 80 ... "
	./httpd.py 80 &
	if [[ $? == 0 ]]; then
		echo " Success";
		pgrep -f httpd.py >> httpd.pid
	else
		echo " Failed";
		rm httpd.pid  >/dev/null 2>&1
	fi
fi

pgrep -f httpsd.py >/dev/null 2>&1
if [[ $? != 0 ]]; then
	echo -e "Starting https service on port 443 ... "
	./httpsd.py 443 &
	if [[ $? == 0 ]]; then
		echo " Success";
		pgrep -f httpsd.py >> httpsd.pid
	else
		echo " Failed";
		rm httpsd.pid  >/dev/null 2>&1
	fi
fi
