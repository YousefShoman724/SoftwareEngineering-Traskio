# Requirements

## Overview
Traskio is a web-based task management system developed using Flask.  
The system provides user authentication (Signup/Login), a protected dashboard, and task management features.  
Data is stored locally using JSON files, and access control is handled through Flask sessions.

---

## Actors
- Guest (Not logged in)
- User (Logged in)

---

## Functional Requirements

### Authentication & User Management
- FR-01: The system shall allow a guest to sign up using an email and password.
- FR-02: The system shall validate that password and confirm password match during signup.
- FR-03: The system shall prevent registration using an already existing email.
- FR-04: The system shall store user passwords in a hashed format.
- FR-05: The system shall allow a registered user to log in using valid credentials.
- FR-06: The system shall reject login attempts with invalid email or password.
- FR-07: The system shall create a user session after successful login.
- FR-08: The system shall allow a logged-in user to log out and clear the session.
- FR-09: The system shall redirect unauthenticated users attempting to access the dashboard to the login page.

---

### Dashboard Access
- FR-10: The system shall provide a protected dashboard accessible only to logged-in users.
- FR-11: The system shall prevent guests from accessing the dashboard route.

---

### Task Management
- FR-12: The system shall allow a logged-in user to view tasks assigned to them.
- FR-13: The system shall allow a logged-in user to create a new task.
- FR-14: The system shall require a task title when creating a task.
- FR-15: The system shall allow a user to edit an existing task.
- FR-16: The system shall allow a user to delete a task.
- FR-17: The system shall store task data in a JSON file.
- FR-18: The system shall associate each task with an assigned user.
- FR-19: The system shall support task attributes such as:
  - Description
  - Status (Pending / In Progress / Completed)
  - Priority
  - Deadline
  - Tags
  - Subtasks
  - Comments

---

### System Utilities
- FR-20: The system shall create required data files if they do not exist.
- FR-21: The system shall allow fixing file permissions to enable read/write access.

---

## Non-Functional Requirements

### Security
- NFR-01: Passwords shall never be stored in plain text.
- NFR-02: User authentication shall be managed using Flask sessions.
- NFR-03: Protected routes shall not be accessible without authentication.

---

### Usability
- NFR-04: The system shall be accessible through a modern web browser.
- NFR-05: The system shall provide clear success and error messages to the user.
- NFR-06: The user interface shall be responsive and easy to use.

---

### Performance & Reliability
- NFR-07: The system shall load tasks efficiently from local JSON storage.
- NFR-08: The system shall handle missing or corrupted data files gracefully.

---

### Testing & Quality
- NFR-09: The system shall include automated unit tests for authentication.
- NFR-10: Automated tests shall run using GitHub Actions (CI pipeline).
- NFR-11: The project repository shall be organized and documented.

---

## Assumptions & Constraints
- The system uses JSON files instead of a database.
- The system is intended for educational and academic use.
- The application runs locally using Flask development server.
