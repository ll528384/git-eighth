import http.server, socketserver, os, sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))
PORT = 8767
Handler = http.server.SimpleHTTPRequestHandler

class NoCache(Handler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

try:
    with socketserver.TCPServer(('0.0.0.0', PORT), NoCache) as httpd:
        print(f'Server running at http://127.0.0.1:{PORT}/')
        httpd.serve_forever()
except OSError:
    print(f'端口 {PORT} 已被占用，请先关掉占用它的程序。')
    sys.exit(1)
