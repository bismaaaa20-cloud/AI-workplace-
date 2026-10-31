from __future__ import annotations

import unittest
from unittest.mock import patch

from app.security import secret_store


class FakeWindowsVault:
    priority = 1


FakeWindowsVault.__module__ = "keyring.backends.Windows"


class SecretStoreTests(unittest.TestCase):
    def setUp(self):
        self.values = {}

    def test_rejects_unknown_provider(self):
        with self.assertRaises(ValueError):
            secret_store.get_api_key("Unknown")

    def test_rejects_newline_and_nul(self):
        with patch.object(secret_store.keyring, "get_keyring", return_value=FakeWindowsVault()):
            for value in ("abc\nxyz", "abc\rxyz", "abc\x00xyz"):
                with self.subTest(value=repr(value)):
                    with self.assertRaises(ValueError):
                        secret_store.save_api_key("Gemini", value)

    def test_rejects_plaintext_or_custom_backend(self):
        class PlaintextBackend:
            priority = 100
        with patch.object(secret_store.keyring, "get_keyring", return_value=PlaintextBackend()):
            with self.assertRaises(RuntimeError):
                secret_store.save_api_key("Gemini", "sample-key")

    def test_secure_backend_save_and_read(self):
        backend = FakeWindowsVault()
        with patch.object(secret_store.keyring, "get_keyring", return_value=backend), patch.object(secret_store.keyring, "set_password", side_effect=lambda service, account, value: self.values.__setitem__((service, account), value)), patch.object(secret_store.keyring, "get_password", side_effect=lambda service, account: self.values.get((service, account))):
            secret_store.save_api_key("Gemini", "sample-key")
            self.assertEqual(secret_store.get_api_key("Gemini"), "sample-key")


if __name__ == "__main__":
    unittest.main()
