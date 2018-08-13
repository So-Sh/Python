from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 8000

#This class will handle any incoming request 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		# Send the html message
		self.wfile.write("<html><body><h2>A simple http server with python</body></html>")
		return

try:
	#Create a web server with the handler to manage the incoming requests
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
