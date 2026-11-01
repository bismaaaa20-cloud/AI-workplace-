import json
import threading
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from app.bridge.server import create_server


class BridgeServerTests(unittest.TestCase):
    def setUp(self):
        self.token = "test-token-" + ("x" * 32)
        self.server = create_server(self.token, port=0)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.base_url = f"http://127.0.0.1:{self.server.server_port}"

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=2)

    def get_json(self, path, *, token=None):
        headers = {}
        if token is not None:
            headers["Authorization"] = f"Bearer {token}"
        request = Request(self.base_url + path, headers=headers)
        with urlopen(request, timeout=2) as response:
            return response.status, json.loads(response.read().decode("utf-8"))

    def test_health_requires_token_and_returns_ok(self):
        with self.assertRaises(HTTPError) as caught:
            urlopen(self.base_url + "/v1/health", timeout=2)
        self.assertEqual(caught.exception.code, 401)
        status, payload = self.get_json("/v1/health", token=self.token)
        self.assertEqual(status, 200)
        self.assertEqual(payload["status"], "ok")

    def test_capabilities_only_expose_discovery_endpoints(self):
        _, payload = self.get_json("/v1/capabilities", token=self.token)
        self.assertTrue(payload["capabilities"]["health"])
        self.assertTrue(payload["capabilities"]["capabilities"])
        self.assertFalse(payload["capabilities"]["chat"])

    def test_chat_endpoint_is_not_implemented(self):
        request = Request(
            self.base_url + "/v1/chat",
            data=b"{}",
            headers={"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"},
            method="POST",
        )
        with self.assertRaises(HTTPError) as caught:
            urlopen(request, timeout=2)
        self.assertEqual(caught.exception.code, 404)

    def test_rejects_non_loopback_bind_address(self):
        with self.assertRaises(ValueError):
            create_server(self.token, host="0.0.0.0", port=0)

    def test_rejects_short_token(self):
        with self.assertRaises(ValueError):
            create_server("short", port=0)


if __name__ == "__main__":
    unittest.main()
