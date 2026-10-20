"""Week 1 starter: a minimal DevOps learning service."""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            payload = {"message": "Hello, DevOps!", "status": "ok"}
            status = 200
        elif self.path == "/health":
            payload = {"status": "ok"}
            status = 200
        else:
            payload = {"error": "not_found", "path": self.path}
            status = 404

        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

def main():
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", "8080"))
    server = HTTPServer((host, port), Handler)
    print(f"DevOps Hello World running at http://{host}:{port}")
    server.serve_forever()

if __name__ == "__main__":
    main()
