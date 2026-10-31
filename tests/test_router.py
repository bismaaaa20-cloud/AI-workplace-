import unittest
from muk.router import Capability, classify_intent, route_message

class RouterTests(unittest.TestCase):
    def setUp(self):
        self.caps = [
            Capability("bugscout", "BugScout gate", "mcp", "Lua script syntax bug check",
                       ("code_debug",), ("lua", "script", "bug"), True, True, "free"),
            Capability("gmail", "Gmail search", "plugin", "Search inbox emails",
                       ("email",), ("gmail", "email"), True, True, "free"),
            Capability("calendar", "Calendar create", "plugin", "Create calendar meeting",
                       ("calendar",), ("meeting", "jadwal"), True, True, "free",
                       read_only=False, requires_confirmation=True),
        ]

    def test_intent(self):
        self.assertEqual(classify_intent("Tolong debug script Lua ini"), "code_debug")

    def test_select_bugscout(self):
        route = route_message("Periksa bug script Lua", self.caps)
        self.assertEqual(route.selected[0]["id"], "bugscout")

    def test_plugin_email(self):
        route = route_message("Cari email proyek di Gmail", self.caps)
        self.assertEqual(route.selected[0]["id"], "gmail")

    def test_write_action_requires_confirmation(self):
        route = route_message("Buat jadwal meeting besok", self.caps)
        self.assertEqual(route.selected[0]["id"], "calendar")
        self.assertIn("calendar", route.needs_confirmation)

    def test_unavailable_is_not_selected(self):
        cap = Capability("off", "Offline tool", "mcp", "Lua bug checker",
                         ("code_debug",), ("lua", "bug"), False, False, "free")
        route = route_message("Periksa bug Lua", [cap])
        self.assertFalse(route.selected)
        self.assertIn("off", route.unavailable_matches)

    def test_paid_excluded_by_default(self):
        cap = Capability("paid", "Paid search", "plugin", "research web search",
                         ("research",), ("research", "search"), True, True, "paid")
        route = route_message("Research AI terbaru", [cap])
        self.assertFalse(route.selected)

if __name__ == "__main__":
    unittest.main()
