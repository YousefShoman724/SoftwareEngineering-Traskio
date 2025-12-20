from flask import Flask, request, jsonify, send_from_directory, session, redirect
from werkzeug.security import generate_password_hash, check_password_hash
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")
USERS_FILE = os.path.join(BASE_DIR, "users.json")

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "change-this-secret-key")

# prevent caching (so edits appear immediately)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

@app.after_request
def no_cache(resp):
    resp.headers["Cache-Control"] = "no-store"
    return resp


# ---------- users helpers ----------
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


# ---------- frontend routes ----------
@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "login.html")

# ✅ NEW: serve styles.css
@app.route("/styles.css")
def styles():
    return send_from_directory(FRONTEND_DIR, "styles.css")

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


# ---------- backend: signup (supports form + json) ----------
@app.route("/signup", methods=["POST"])
def signup():
    if request.is_json:
        data = request.get_json(silent=True) or {}
        email = norm_email(data.get("email"))
        password = data.get("password") or ""
        confirm = data.get("confirm_password") or data.get("confirmPassword") or ""
    else:
        email = norm_email(request.form.get("email"))
        password = request.form.get("password") or ""
        confirm = request.form.get("confirm_password") or ""

    if not email or not password:
        msg = "Missing email or password"
        return (jsonify({"success": False, "message": msg}), 400) if request.is_json else redirect(f"/signup_page?msg={msg}")

    if confirm and confirm != password:
        msg = "Passwords do not match"
        return (jsonify({"success": False, "message": msg}), 400) if request.is_json else redirect(f"/signup_page?msg={msg}")

    users = load_users()
    if any(norm_email(u.get("email")) == email for u in users):
        msg = "Email already exists"
        return (jsonify({"success": False, "message": msg}), 409) if request.is_json else redirect(f"/signup_page?msg={msg}")

    users.append({"email": email, "password": generate_password_hash(password)})
    save_users(users)

    msg = "Signup successful. Please login."
    return jsonify({"success": True, "message": msg}) if request.is_json else redirect(f"/?msg={msg}")


# ---------- backend: login (supports form + json) ----------
@app.route("/login", methods=["POST"])
def login():
    if request.is_json:
        data = request.get_json(silent=True) or {}
        email = norm_email(data.get("email"))
        password = data.get("password") or ""
    else:
        email = norm_email(request.form.get("email"))
        password = request.form.get("password") or ""

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

            # auto-upgrade plain text -> hashed
            if not is_hashed(stored_pw):
                u["password"] = generate_password_hash(password)
                save_users(users)

            if request.is_json:
                return jsonify({"success": True, "message": "Login successful", "redirect": "/dashboard"})
            return redirect("/dashboard")

        break

    msg = "Invalid email or password"
    return (jsonify({"success": False, "message": msg}), 401) if request.is_json else redirect(f"/?msg={msg}")


if __name__ == "__main__":
    app.run(debug=True)
