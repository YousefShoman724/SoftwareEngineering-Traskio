from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

TASKS_FILE = "tasks.json"

# =======================
# Helpers
# =======================
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w") as f:
            json.dump([], f)
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def get_next_id(tasks):
    return max([t["id"] for t in tasks], default=0) + 1

# =======================
# Routes
# =======================

# Serve dashboard
@app.route("/")
def index():
    return send_from_directory(os.getcwd(), "index.html")

# Get all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(load_tasks())

# Add task
@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    tasks = load_tasks()

    task = {
        "id": get_next_id(tasks),
        "title": data.get("title", ""),
        "description": data.get("description", ""),
        "assigned_to": data.get("assigned_to", ""),
        "status": data.get("status", "Pending")
    }

    if not task["title"]:
        return jsonify({"error": "Title is required"}), 400

    tasks.append(task)
    save_tasks(tasks)

    return jsonify(task), 201

# Update task
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    tasks = load_tasks()
    data = request.json

    for task in tasks:
        if task["id"] == task_id:
            task.update(data)
            save_tasks(tasks)
            return jsonify(task)

    return jsonify({"error": "Task not found"}), 404

# Delete task
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    return jsonify({"message": "Deleted"}), 200

# =======================
if __name__ == "__main__":
    app.run(debug=True)
