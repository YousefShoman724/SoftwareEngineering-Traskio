from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

USERS_FILE = "users.json"

# التأكد من وجود الملف
if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, "w") as f:
        json.dump([], f)

# ----------------------------
# Helper functions
# ----------------------------
def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return []

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

# ----------------------------
# Frontend routes
# ----------------------------
@app.route("/")
def home():
    return send_from_directory("frontend", "login.html")

@app.route("/signup_page")
def signup_page():
    return send_from_directory("frontend", "signup.html")

# ----------------------------
# Backend routes
# ----------------------------
@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"message": "Signup failed: Missing email or password"})

    users = load_users()
    if any(u["email"] == email for u in users):
        return jsonify({"message": "Email already exists!"})

    users.append({"email": email, "password": password})
    save_users(users)
    return jsonify({"message": "Signup successful"})

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    users = load_users()
    for u in users:
        if u["email"] == email and u["password"] == password:
            return jsonify({"message": "Login successful", "success": True})
    return jsonify({"message": "Invalid email or password", "success": False})

# ----------------------------
# Run server
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)
