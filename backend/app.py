from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory task storage
tasks = []
next_id = 1  # Auto-increment ID for tasks


# Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200


# Add a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    global next_id
    data = request.json

    # Validate required fields
    required_fields = ['title', 'description', 'assigned_to', 'status']
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({"error": f"{field} is required"}), 400

    # Create task object
    task = {
        "id": next_id,
        "title": data['title'],
        "description": data['description'],
        "assigned_to": data['assigned_to'],
        "status": data['status']
    }
    tasks.append(task)
    next_id += 1

    return jsonify({"message": "Task added successfully", "task": task}), 201


# Update an existing task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    # Update allowed fields
    for key in ['title', 'description', 'assigned_to', 'status']:
        if key in data:
            task[key] = data[key]

    return jsonify({"message": "Task updated successfully", "task": task}), 200


# Delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({"message": "Task deleted successfully"}), 200


# Simple login/logout simulation
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if data.get("username") == "user1" and data.get("password") == "pass123":
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/logout', methods=['POST'])
def logout():
    return jsonify({"message": "Logout successful"}), 200


if __name__ == '__main__':
    app.run(debug=True)
