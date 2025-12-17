## UC-05: Create Task

**Actor:** User  

**Description:**  
Allows the user to create a new task.

**Preconditions:**
- User is logged in.

**Main Flow:**
1. User enters task details.
2. User submits the task.
3. System generates a task ID.
4. Task is saved in `tasks.json`.

**Alternative Flow:**
- Task title is missing → system shows an error.

**Postconditions:**
- New task is created.

---
