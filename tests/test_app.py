import unittest
import json
from main import app, USERS_FILE
import os

class TestAuth(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # نعمل نسخة فارغة من users.json لكل اختبار
        with open(USERS_FILE, "w") as f:
            json.dump([], f)

    def test_signup_success(self):
        response = self.app.post("/signup", json={
            "email": "test1@example.com",
            "password": "123456"
        })
        data = json.loads(response.data)
        self.assertEqual(data["message"], "Signup successful")
    
    def test_signup_existing_email(self):
        # نسجل أول مرة
        self.app.post("/signup", json={
            "email": "test2@example.com",
            "password": "123456"
        })
        # نحاول نسجل بنفس الإيميل
        response = self.app.post("/signup", json={
            "email": "test2@example.com",
            "password": "123456"
        })
        data = json.loads(response.data)
        self.assertIn("already exists", data["message"])

    def test_login_success(self):
        # نسجل أولاً
        self.app.post("/signup", json={
            "email": "test3@example.com",
            "password": "123456"
        })
        # نسجل دخول
        response = self.app.post("/login", json={
            "email": "test3@example.com",
            "password": "123456"
        })
        data = json.loads(response.data)
        self.assertIn("Login successful", data["message"])

    def test_login_invalid(self):
        response = self.app.post("/login", json={
            "email": "wrong@example.com",
            "password": "0000"
        })
        data = json.loads(response.data)
        self.assertIn("Invalid", data["message"])

    def test_signup_missing_fields(self):
        response = self.app.post("/signup", json={
            "email": "",
            "password": ""
        })
        data = json.loads(response.data)
        self.assertIn("Missing email or password", data["message"])

if __name__ == "__main__":
    unittest.main()
