from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return send_from_directory('', 'login.html')  # هيفتح login.html مباشرة

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    if email == "test@test.com" and password == "1234":
        return jsonify({"message": "Login successful"})
    return jsonify({"message": "Invalid credentials"})

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')        
    if email and password:
        return jsonify({"message": "Signup successful"})
    return jsonify({"message": "Signup failed"})

if __name__ == "__main__":
    app.run(debug=True)
