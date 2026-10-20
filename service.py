"""Reusable request-routing logic for the Week 3 DevOps practice project."""
import json

APP_VERSION = "3.0.0"

def response_for_path(path: str):
    """Return (status_code, payload) for a requested URL path."""
    if path == "/":
        return 200, {"message": "Hello, DevOps!", "version": APP_VERSION}
    if path == "/health":
        return 200, {"status": "ok", "version": APP_VERSION}
    if path == "/version":
        return 200, {"version": APP_VERSION}
    return 404, {"error": "not_found", "path": path}

def json_bytes(payload):
    """Serialize a payload as UTF-8 JSON bytes."""
    return json.dumps(payload).encode("utf-8")
