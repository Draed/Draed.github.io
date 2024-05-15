import http.server
import socketserver

PORT = 8000

# Define a simple HTTP request handler
class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

# Create a TCP server
with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print("Serving tiny webserver at port", PORT)
    httpd.serve_forever()