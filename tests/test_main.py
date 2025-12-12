import unittest
import json
import os
import tempfile

import main
from main import app


class TestAuth(unittest.TestCase):
    def setUp(self):
        app.config.update(TESTING=True, SECRET_KEY="test-secret")

        # Temp users file (does NOT touch your real users.json)
        self.tmpdir = tempfile.TemporaryDirectory()
        self.temp_users_file = os.path.join(self.tmpdir.name, "users.json")
        with open(self.temp_users_file, "w", encoding="utf-8") as f:
            json.dump([], f)

        main.USERS_FILE = self.temp_users_file
        self.client = app.test_client()

    def tearDown(self):
        self.tmpdir.cleanup()

    def test_signup_success(self):
        r = self.client.post("/signup", json={
            "email": "test1@example.com",
            "password": "123456",
            "confirm_password": "123456"
        })
        data = r.get_json()
        self.assertTrue(data["success"])
        self.assertIn("Signup successful", data["message"])

    def test_signup_existing_email(self):
        self.client.post("/signup", json={
            "email": "test2@example.com",
            "password": "123456",
            "confirm_password": "123456"
        })

        r = self.client.post("/signup", json={
            "email": "test2@example.com",
            "password": "123456",
            "confirm_password": "123456"
        })
        data = r.get_json()
        self.assertFalse(data["success"])
        self.assertIn("exists", data["message"].lower())

    def test_login_success(self):
        self.client.post("/signup", json={
            "email": "test3@example.com",
            "password": "123456",
            "confirm_password": "123456"
        })

        r = self.client.post("/login", json={
            "email": "test3@example.com",
            "password": "123456"
        })
        data = r.get_json()
        self.assertTrue(data["success"])
        self.assertIn("login successful", data["message"].lower())

    def test_login_invalid(self):
        r = self.client.post("/login", json={
            "email": "wrong@example.com",
            "password": "0000"
        })
        data = r.get_json()
        self.assertFalse(data["success"])
        self.assertIn("invalid", data["message"].lower())

    def test_dashboard_requires_login(self):
        r = self.client.get("/dashboard", follow_redirects=False)
        self.assertIn(r.status_code, (301, 302))

    def test_dashboard_after_login(self):
        self.client.post("/signup", json={
            "email": "dash@test.com",
            "password": "123456",
            "confirm_password": "123456"
        })
        self.client.post("/login", json={
            "email": "dash@test.com",
            "password": "123456"
        })
        r = self.client.get("/dashboard", follow_redirects=False)
        self.assertEqual(r.status_code, 200)


if __name__ == "__main__":
    unittest.main()
