from backend.main import app

# optional: for local run (Render uses gunicorn)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
