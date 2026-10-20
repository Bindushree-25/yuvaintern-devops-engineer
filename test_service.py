"""Automated unit tests for the Week 3 request-routing logic."""
import unittest
from app.service import APP_VERSION, response_for_path, json_bytes

class ResponseForPathTests(unittest.TestCase):
    def test_root_route(self):
        status, payload = response_for_path("/")
        self.assertEqual(status, 200)
        self.assertEqual(payload["message"], "Hello, DevOps!")
        self.assertEqual(payload["version"], APP_VERSION)

    def test_health_route(self):
        status, payload = response_for_path("/health")
        self.assertEqual(status, 200)
        self.assertEqual(payload["status"], "ok")
        self.assertEqual(payload["version"], APP_VERSION)

    def test_version_route(self):
        status, payload = response_for_path("/version")
        self.assertEqual(status, 200)
        self.assertEqual(payload["version"], APP_VERSION)

    def test_unknown_route(self):
        status, payload = response_for_path("/missing")
        self.assertEqual(status, 404)
        self.assertEqual(payload["error"], "not_found")
        self.assertEqual(payload["path"], "/missing")

    def test_json_serialization_returns_bytes(self):
        result = json_bytes({"status": "ok"})
        self.assertIsInstance(result, bytes)
        self.assertIn(b'"status": "ok"', result)

if __name__ == "__main__":
    unittest.main()
