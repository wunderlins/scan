#!/usr/bin/env python

import web, os, re
from web.wsgiserver import CherryPyWSGIServer

CherryPyWSGIServer.ssl_certificate = "../cert/cert.pem"
CherryPyWSGIServer.ssl_private_key = "../cert/key_server.pem"

urls = (
  '/', 'index'
)

class index:
	def GET(self):
		# open static index file, read it and return it
		#print os.path.dirname(os.path.realpath(__file__))
		fp = open('static/MainWindow/index.html', 'r')
		content = fp.read()
		fp.close()
		
		# inject base tag after opening head tag
		base = '<base href="/static/MainWindow/" target="_blank">'
		content = content.replace("<head>", "<head>" + base);
		
		# sencha architect is unable to set the title tag properly, do it here! WTF
		reg = re.compile( '<title>[^<]+</title>')
		content = reg.sub("<title>Scan Station</title>", content)
		
		return content
		
if __name__ == "__main__": 
	app = web.application(urls, globals())
	app.run()
