"""Unit tests for expected route behavior and response contracts."""
import unittest
from app.service import APP_VERSION, response_for_path, validate_response

class RouteTests(unittest.TestCase):
    def test_root_success_contract(self):
        status, payload = response_for_path("/")
        self.assertEqual(status, 200)
        self.assertEqual(payload, {"message": "Hello, DevOps!", "version": APP_VERSION})
        self.assertEqual(validate_response(status, payload)[0], True)

    def test_health_success_contract(self):
        status, payload = response_for_path("/health")
        self.assertEqual(status, 200)
        self.assertEqual(payload["status"], "ok")
        self.assertEqual(validate_response(status, payload)[0], True)

    def test_version_success_contract(self):
        status, payload = response_for_path("/version")
        self.assertEqual(status, 200)
        self.assertEqual(payload["version"], APP_VERSION)

    def test_unknown_route_returns_404(self):
        status, payload = response_for_path("/unknown")
        self.assertEqual(status, 404)
        self.assertEqual(payload["error"], "not_found")
        self.assertEqual(payload["path"], "/unknown")
        self.assertEqual(validate_response(status, payload)[0], True)

    def test_contract_rejects_non_integer_status(self):
        ok, message = validate_response("200", {"message": "ok"})
        self.assertFalse(ok)
        self.assertEqual(message, "status must be an integer")

    def test_contract_rejects_non_dictionary_payload(self):
        ok, message = validate_response(200, ["not", "a", "dictionary"])
        self.assertFalse(ok)
        self.assertEqual(message, "payload must be a dictionary")

    def test_contract_rejects_empty_success_payload(self):
        ok, message = validate_response(200, {})
        self.assertFalse(ok)
        self.assertEqual(message, "successful response payload must not be empty")

    def test_contract_rejects_malformed_404(self):
        ok, message = validate_response(404, {"error": "missing"})
        self.assertFalse(ok)
        self.assertEqual(message, "404 response must identify not_found")

if __name__ == "__main__":
    unittest.main()
