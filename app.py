from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT=8000

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Baby oil :D, Python code for this page')
    
    httpd= HTTPServer(('',PORT), MyHandler)
    print(f'Running on port {PORT}...')
    httpd.serve_forever()    
