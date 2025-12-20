from flask import Flask, request, jsonify, send_from_directory, session, redirect
from werkzeug.security import generate_password_hash, check_password_hash
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "../frontend")
USERS_FILE = os.path.join(BASE_DIR, "users.json")
TASKS_FILE = os.path.join(BASE_DIR, "tasks.json")

# ---------------- Task helpers ----------------
def ensure_tasks_file():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)

def load_tasks():
    ensure_tasks_file()
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

# ---------------- Flask app ----------------
app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "change-this-secret-key")
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

@app.after_request
def no_cache(resp):
    resp.headers["Cache-Control"] = "no-store"
    return resp

# ---------------- User helpers ----------------
def ensure_users_file():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)

def load_users():
    ensure_users_file()
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return []

def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4, ensure_ascii=False)

def is_hashed(pw: str) -> bool:
    return isinstance(pw, str) and (pw.startswith("pbkdf2:") or pw.startswith("scrypt:"))

def norm_email(email: str) -> str:
    return (email or "").strip().lower()

# ---------------- Frontend routes ----------------
@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "login.html")

@app.route("/signup_page")
def signup_page():
    return send_from_directory(FRONTEND_DIR, "signup.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")
    return send_from_directory(FRONTEND_DIR, "dashboard.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/me")
def me():
    if "user" not in session:
        return jsonify({"logged_in": False}), 401
    return jsonify({"logged_in": True, "email": session["user"]})

# ---------------- Signup ----------------
@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json(silent=True) or request.form
    email = norm_email(data.get("email"))
    password = data.get("password") or ""
    confirm = data.get("confirm_password") or data.get("confirmPassword") or ""

    if not email or not password:
        msg = "Missing email or password"
        return (jsonify({"success": False, "message": msg}), 400)

    if confirm and confirm != password:
        msg = "Passwords do not match"
        return (jsonify({"success": False, "message": msg}), 400)

    users = load_users()
    if any(norm_email(u.get("email")) == email for u in users):
        msg = "Email already exists"
        return (jsonify({"success": False, "message": msg}), 409)

    users.append({"email": email, "password": generate_password_hash(password)})
    save_users(users)

    msg = "Signup successful. Please login."
    return jsonify({"success": True, "message": msg})

# ---------------- Login ----------------
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or request.form
    email = norm_email(data.get("email"))
    password = data.get("password") or ""

    users = load_users()
    for u in users:
        if norm_email(u.get("email")) != email:
            continue

        stored_pw = u.get("password") or ""
        if is_hashed(stored_pw):
            ok = check_password_hash(stored_pw, password)
        else:
            ok = (stored_pw == password)

        if ok:
            session["user"] = email

            if not is_hashed(stored_pw):
                u["password"] = generate_password_hash(password)
                save_users(users)

            return jsonify({"success": True, "message": "Login successful", "redirect": "/dashboard"})

    msg = "Invalid email or password"
    return (jsonify({"success": False, "message": msg}), 401)

# ---------------- Task APIs ----------------
@app.route("/tasks", methods=["GET"])
def get_tasks():
    if "user" not in session:
        return jsonify({"success": False, "message": "Not logged in"}), 401
    user_email = session["user"]
    tasks = load_tasks()
    user_tasks = [t for t in tasks if t.get("assigned_to") == user_email]
    return jsonify(user_tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    if "user" not in session:
        return jsonify({"success": False, "message": "Not logged in"}), 401
    data = request.get_json(silent=True) or request.form
    if not data.get("title"):
        return jsonify({"success": False, "message": "Task title is required"}), 400

    tasks = load_tasks()
    task_id = max([t.get("id", 0) for t in tasks], default=0) + 1
    new_task = {
        "id": task_id,
        "title": data.get("title"),
        "description": data.get("description", ""),
        "assigned_to": data.get("assigned_to") or session["user"],
        "status": data.get("status", "Pending"),
        "deadline": data.get("deadline"),
        "priority": data.get("priority", "Medium"),
        "tags": data.get("tags", []),
        "subtasks": [],
        "comments": [],
        "createdAt": data.get("createdAt"),
        "timeTracked": 0
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return jsonify({"success": True, "message": "Task added successfully", "task": new_task})

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def edit_task(task_id):
    if "user" not in session:
        return jsonify({"success": False, "message": "Not logged in"}), 401
    data = request.get_json(silent=True) or request.form
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["title"] = data.get("title", t["title"])
            t["description"] = data.get("description", t["description"])
            t["status"] = data.get("status", t.get("status", "In Progress"))
            t["assigned_to"] = data.get("assigned_to", t.get("assigned_to"))
            t["deadline"] = data.get("deadline", t.get("deadline"))
            t["priority"] = data.get("priority", t.get("priority", "Medium"))
            t["tags"] = data.get("tags", t.get("tags", []))
            t["subtasks"] = data.get("subtasks", t.get("subtasks", []))
            t["comments"] = data.get("comments", t.get("comments", []))
            t["timeTracked"] = data.get("timeTracked", t.get("timeTracked", 0))
            save_tasks(tasks)
            return jsonify({"success": True, "message": "Task updated successfully"})
    return jsonify({"success": False, "message": "Task not found"}), 404

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    if "user" not in session:
        return jsonify({"success": False, "message": "Not logged in"}), 401
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    return jsonify({"success": True, "message": "Task deleted successfully"})

# ---------------- Users API ----------------
@app.route("/users", methods=["GET"])
def get_users():
    if "user" not in session:
        return jsonify([]), 401
    users = load_users()
    return jsonify([u["email"] for u in users])

# ---------------- Run server ----------------
if __name__ == "__main__":
    app.run(debug=True)