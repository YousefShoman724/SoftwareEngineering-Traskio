from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)

USERS_FILE = "users.json"

# التأكد من وجود الملف
if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, "w") as f:
        json.dump([], f)

# فتح login.html عند /
@app.route('/')
def index():
    return send_from_directory('', 'login.html')

# فتح signup.html عند /signup
@app.route('/signup')
def signup_page():
    return send_from_directory('frontend', 'signup.html')

# API تسجيل الدخول
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    with open(USERS_FILE, "r") as f:
        users = json.load(f)

    for user in users:
        if user["email"] == email and user["password"] == password:
            return jsonify({"message": "Login successful"})
    return jsonify({"message": "Invalid credentials"})

# API تسجيل جديد
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')        

    if not email or not password:
        return jsonify({"message": "Signup failed: Missing email or password"})

    with open(USERS_FILE, "r") as f:
        users = json.load(f)

    for user in users:
        if user["email"] == email:
            return jsonify({"message": "Signup failed: Email already exists"})

    users.append({"email": email, "password": password})

    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

    return jsonify({"message": "Signup successful"})

if __name__ == "__main__":
    app.run(debug=True)
