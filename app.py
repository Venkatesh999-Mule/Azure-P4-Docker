import os
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html_content = '''
            <html>
            <body style="font-family:Arial; text-align:center; padding:50px; background:#f0f8ff">
                <h1>Hello from Docker Container! 🐳</h1>
                <p>Web Server running inside Docker on Azure!</p>
                <p style="color:green">Container is healthy and running!</p>
            </body>
            </html>
            '''
            
            self.wfile.write(html_content.encode('utf-8'))
            
        elif self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Healthy!')

    def log_message(self, format, *args):
        print(f"Request: {args}")

if __name__ == '__main__':
    port = int(os.environ.get('WEBSITES_PORT', os.environ.get('PORT', 8080)))
    server = HTTPServer(('0.0.0.0', port), SimpleHandler)
    print(f'Server running on port {port}...')
    server.serve_forever()
