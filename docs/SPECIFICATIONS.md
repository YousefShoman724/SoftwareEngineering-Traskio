# Traskio Project – Full Specifications

---

## 1. Project Overview
**Traskio** is a full-stack **web-based task management application** designed to help users efficiently manage personal and collaborative tasks. The system provides features for:

- User registration and secure login
- Creating, editing, deleting, and viewing tasks
- Managing subtasks, comments, tags, and deadlines
- Time tracking for tasks
- Viewing dashboard summaries and statistics

**Technology Stack**:
- Backend: Python Flask
- Frontend: HTML, CSS, JavaScript
- Storage: JSON files (`users.json`, `tasks.json`)
- Communication: RESTful APIs (JSON)

The project emphasizes **security**, **usability**, and **modular design**, ensuring easy maintenance and future scalability.

---

## 2. System Components

### 2.1 Frontend Components
1. **Signup Page**
   - Form fields: Email, Password, Confirm Password
   - Validates user input and communicates with `/signup` API
2. **Login Page**
   - Email and password fields
   - Communicates with `/login` API
   - Handles session initialization
3. **Dashboard**
   - Displays task list, statistics, and navigation to task details
   - Provides logout button
4. **Task List Component**
   - Lists all tasks of logged-in user
   - Allows edit, delete, view details
5. **Task Form Component**
   - Used for adding or editing tasks
   - Fields: Title, Description, Priority, Deadline
6. **Task Details Component**
   - Shows subtasks, comments, tags, and time tracking
7. **Time Tracking Component**
   - Start/Stop timer per task
   - Displays total time tracked

### 2.2 Backend Components
1. **Authentication Module**
   - Handles signup, login, and logout
   - Password hashing using secure algorithms
   - Session management for logged-in users
2. **Task Management Module**
   - Handles CRUD operations for tasks
   - Subtasks, comments, tags, deadlines
   - Time tracking operations
3. **API Layer**
   - Provides RESTful JSON endpoints
   - Validates input and provides appropriate responses
4. **Storage Management**
   - Reads/writes `users.json` and `tasks.json`
   - Ensures data integrity and consistency

---

## 3. Functional Requirements

### 3.1 User Management
- **Signup**:
  - Input validation (valid email, password strength, password confirmation)
  - Duplicate emails rejected
  - Passwords stored hashed
- **Login**:
  - Valid credentials grant access
  - Invalid credentials produce errors
- **Logout**:
  - Ends session
  - Restricts dashboard access

### 3.2 Task Management
- **Create Task**: Title, description, priority, optional deadline
- **Edit Task**: Modify any task attribute
- **Delete Task**: Remove task permanently
- **View Task**: Full task details including subtasks, comments, tags
- **Subtasks**: Add/manage subtasks under a main task
- **Comments & Tags**: Add, view, and edit
- **Time Tracking**: Start/stop timer and store duration

### 3.3 Dashboard
- Displays task statistics: total tasks, pending, completed
- Accessible only to authenticated users

### 3.4 API Endpoints
| Endpoint             | Method | Description                              | Request Body / Params                         | Response |
|---------------------|--------|------------------------------------------|-----------------------------------------------|----------|
| `/signup`            | POST   | Register new user                         | `{ "email": "...", "password": "...", "confirm_password": "..." }` | Status 200/400 JSON |
| `/login`             | POST   | Authenticate user                         | `{ "email": "...", "password": "..." }`       | Status 200/401 JSON |
| `/logout`            | GET    | End session                               | -                                             | Redirect |
| `/tasks`             | GET    | List all user tasks                        | -                                             | JSON array |
| `/tasks`             | POST   | Create task                               | `{ "title": "...", "description": "...", "assigned_to": "...", "status": "..." }` | Status 201/400 |
| `/tasks/{id}`        | PUT    | Update task                               | `{ "title": "...", "description": "...", "status": "..." }` | Status 200 |
| `/tasks/{id}`        | DELETE | Delete task                               | -                                             | Status 200 |

---

## 4. Non-Functional Requirements

- **Security**
  - Password hashing
  - Session management
  - Restricted dashboard access
- **Performance**
  - Task CRUD operations <2 seconds
  - Dashboard load <3 seconds
- **Usability**
  - Intuitive UI
  - Clear error/validation messages
- **Maintainability**
  - Modular backend
  - Reusable frontend components
  - JSON structured data for easy migration
- **Scalability**
  - Design allows migration to relational DB in future

---

## 5. System Constraints

- Backend: Python Flask
- Frontend: Vanilla HTML/CSS/JS
- Data Storage: JSON files only
- Runs locally on `http://127.0.0.1:5000`
- No external database required

---

## 6. User Roles

1. **Registered User**
   - Full access to tasks and dashboard
   - Add/edit/delete tasks
   - Manage subtasks, comments, tags
   - Track time

2. **Guest**
   - Access limited to Signup/Login
   - Cannot view dashboard or tasks

---

## 7. User Stories
1. As a user, I can sign up to create an account.
2. As a user, I can log in and log out securely.
3. As a user, I can create, edit, and delete tasks.
4. As a user, I can manage subtasks, comments, and tags for tasks.
5. As a user, I can track time spent on tasks.
6. As a user, I can view dashboard statistics of my tasks.

---

## 8. Use Cases
- **Signup / Login**
- **Task CRUD**
- **Subtasks Management**
- **Comments & Tags**
- **Time Tracking**
- **Dashboard Overview**

---

## 9. Assumptions
- Users have a stable internet connection.
- Users use modern browsers that support HTML5, CSS3, and JS.
- Time tracking does not require persistence across multiple devices (local storage suffices for now).

---

## 10. Glossary
- **CRUD**: Create, Read, Update, Delete
- **API**: Application Programming Interface
- **JSON**: JavaScript Object Notation

---

## 11. Test Cases

### 11.1 Authentication Test Cases
| Test Case ID | Title                  | Description                                   | Steps                                               | Expected Result              |
|--------------|-----------------------|-----------------------------------------------|----------------------------------------------------|------------------------------|
| TC-01        | Signup with Valid Data | Verify new user can sign up with valid email | Enter valid email/password → Submit               | Success, redirected to login |
| TC-02        | Signup Duplicate Email | Prevent duplicate registrations               | Enter existing email → Submit                      | Error message displayed      |
| TC-03        | Login Valid Credentials| Verify login functionality                    | Enter valid credentials → Submit                   | Access dashboard             |
| TC-04        | Login Invalid Credentials | Prevent unauthorized login                  | Enter wrong email/password → Submit               | Error message displayed      |
| TC-05        | Logout                | End session                                   | Click logout button                                 | Redirect to login page       |

### 11.2 Task Management Test Cases
| Test Case ID | Title                  | Description                                   | Steps                                               | Expected Result              |
|--------------|-----------------------|-----------------------------------------------|----------------------------------------------------|------------------------------|
| TC-06        | Create Task           | Add new task                                  | Open dashboard → Add task → Submit                 | Task appears in list         |
| TC-07        | Edit Task             | Update task details                           | Select task → Edit → Save                          | Task updated                 |
| TC-08        | Delete Task           | Remove task                                   | Select task → Delete                               | Task removed                 |
| TC-09        | Add Subtask           | Add subtask under task                        | Open task → Add subtask → Save                     | Subtask visible              |
| TC-10        | Track Time            | Start/stop timer                              | Start timer → Stop timer                            | Duration stored correctly    |

---

## 12. Diagrams

### 12.1 UML Diagrams
- **Use Case Diagram:** Shows interactions between users and system features (signup, login, task CRUD, dashboard, etc.)
- **Class Diagram:** Represents structure of backend and frontend components with their relationships.
- **Sequence Diagrams:** Demonstrates flow of actions for main features like signup, login, task creation.
- **Component Diagram:** Illustrates frontend and backend modules and their connections.
- **State Diagram:** Shows states of a task (Pending, In Progress, Completed).

### 12.2 Notes
- Diagrams are designed for clarity, maintainability, and to aid understanding of system architecture.
- All components and interactions are represented according to the current implementation of Traskio.

---

## 13. GitHub Repository Structure

### 13.1 Repository Organization
- **Frontend:** Contains HTML, CSS, JS files
- **Backend:** Contains Flask app, API endpoints
- **Data:** `users.json`, `tasks.json`
- **Docs:** Project documentation, diagrams, specifications
- **Tests:** Test cases and testing scripts
- **.github/workflows:** CI/CD pipeline configuration
