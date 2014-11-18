#!/usr/bin/env python

import web
from web.wsgiserver import CherryPyWSGIServer

CherryPyWSGIServer.ssl_certificate = "../cert/cert.pem"
CherryPyWSGIServer.ssl_private_key = "../cert/key_server.pem"

urls = (
  '/', 'index'
)

class index:
	def GET(self):
		return "Hello, world!"
		
if __name__ == "__main__": 
	app = web.application(urls, globals())
	app.run()
