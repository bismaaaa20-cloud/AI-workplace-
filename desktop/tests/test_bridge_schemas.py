import unittest

from app.bridge.schemas import (
    PROTOCOL_VERSION,
    ProtocolValidationError,
    capabilities_payload,
    health_payload,
    validate_chat_request,
    validate_chat_response,
)


class BridgeSchemaTests(unittest.TestCase):
    def test_health_payload_uses_protocol_version(self):
        self.assertEqual(health_payload()["protocol_version"], PROTOCOL_VERSION)
        self.assertEqual(health_payload()["status"], "ok")

    def test_capabilities_do_not_advertise_unimplemented_features(self):
        capabilities = capabilities_payload()["capabilities"]
        self.assertTrue(capabilities["health"])
        self.assertTrue(capabilities["capabilities"])
        for feature in ("chat", "planning", "task_decomposition", "tool_use", "streaming", "persistent_memory"):
            self.assertFalse(capabilities[feature])

    def test_valid_future_chat_request(self):
        payload = {
            "protocol_version": PROTOCOL_VERSION,
            "request_id": "req-001",
            "message": "hello",
            "context": [],
            "mode": "direct",
        }
        result = validate_chat_request(payload)
        self.assertEqual(result["request_id"], "req-001")
        self.assertIsNone(result["session_id"])

    def test_rejects_wrong_protocol_version(self):
        with self.assertRaises(ProtocolValidationError):
            validate_chat_request({"protocol_version": "v0", "request_id": "r1", "message": "hello"})

    def test_rejects_malformed_request(self):
        with self.assertRaises(ProtocolValidationError):
            validate_chat_request({"protocol_version": PROTOCOL_VERSION, "request_id": "bad id", "message": "hello"})

    def test_rejects_unknown_request_fields(self):
        with self.assertRaises(ProtocolValidationError):
            validate_chat_request({
                "protocol_version": PROTOCOL_VERSION,
                "request_id": "r1",
                "message": "hello",
                "made_up": True,
            })

    def test_validates_future_chat_response_request_id(self):
        response = {
            "protocol_version": PROTOCOL_VERSION,
            "request_id": "r1",
            "status": "completed",
            "answer": "hello",
            "tasks": [],
            "error": None,
        }
        self.assertEqual(validate_chat_response(response, expected_request_id="r1")["answer"], "hello")

    def test_rejects_mismatched_response_request_id(self):
        response = {
            "protocol_version": PROTOCOL_VERSION,
            "request_id": "r2",
            "status": "completed",
            "answer": "hello",
        }
        with self.assertRaises(ProtocolValidationError):
            validate_chat_response(response, expected_request_id="r1")


if __name__ == "__main__":
    unittest.main()
