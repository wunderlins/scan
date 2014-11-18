#!/usr/bin/env python

import web
urls = (
  '/', 'index'
)

class index:
	def GET(self):
		# TODO do a redirect to https
		return "<script>document.location.href = 'https://' + document.location.hostname;</script>"
		
if __name__ == "__main__": 
	app = web.application(urls, globals())
	app.run()
