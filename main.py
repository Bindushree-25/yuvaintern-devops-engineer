"""Small standard-library HTTP service for practicing DevOps core concepts.

Run: python app/main.py
Routes:
  GET /          -> JSON welcome response
  GET /health    -> JSON health response
  GET /version   -> JSON application version
"""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

APP_VERSION = "2.0.0"

class Handler(BaseHTTPRequestHandler):
    def _send_json(self, status_code, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/":
            self._send_json(200, {"message": "Hello, DevOps!", "version": APP_VERSION})
        elif self.path == "/health":
            self._send_json(200, {"status": "ok", "version": APP_VERSION})
        elif self.path == "/version":
            self._send_json(200, {"version": APP_VERSION})
        else:
            self._send_json(404, {"error": "not_found", "path": self.path})

    def log_message(self, format, *args):
        print("%s - %s" % (self.address_string(), format % args))

if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8000), Handler)
    print("DevOps practice service listening at http://127.0.0.1:8000")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
    finally:
        server.server_close()
