"""Testable route logic for the Week 4 QA practice project."""
APP_VERSION = "4.0.0"

def response_for_path(path: str):
    """Return the expected HTTP status and JSON-compatible payload for a path."""
    if path == "/":
        return 200, {"message": "Hello, DevOps!", "version": APP_VERSION}
    if path == "/health":
        return 200, {"status": "ok", "version": APP_VERSION}
    if path == "/version":
        return 200, {"version": APP_VERSION}
    return 404, {"error": "not_found", "path": path}

def validate_response(status, payload):
    """Basic contract validation used by tests and examples."""
    if not isinstance(status, int):
        return False, "status must be an integer"
    if not isinstance(payload, dict):
        return False, "payload must be a dictionary"
    if status == 200 and not payload:
        return False, "successful response payload must not be empty"
    if status == 404 and payload.get("error") != "not_found":
        return False, "404 response must identify not_found"
    return True, "response contract accepted"
