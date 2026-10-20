"""Run the Week 3 practice service with: python -m app.main"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from app.service import response_for_path, json_bytes

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        status, payload = response_for_path(self.path)
        body = json_bytes(payload)
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        print("%s - %s" % (self.address_string(), format % args))

if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8000), Handler)
    print("Week 3 practice service listening at http://127.0.0.1:8000")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
    finally:
        server.server_close()
