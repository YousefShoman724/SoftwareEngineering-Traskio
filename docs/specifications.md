# Software Specifications — Traskio Phase 2

## 1. Purpose
This document defines the technical specifications for the Traskio web application.
The system provides user authentication and task management using a Flask backend
and a browser-based frontend.

## 2. System Overview
Traskio is a web-based task management system that allows users to:
- Sign up and log in securely
- Access a protected dashboard
- Create, view, edit, and delete tasks
- Assign tasks to users
- Filter, search, and sort tasks

## 3. System Architecture
The system follows a simple client–server architecture:

- Frontend: HTML, CSS, JavaScript (served as static files)
- Backend: Flask (Python)
- Data Storage: JSON files (users.json, tasks.json)
- Session Management: Flask sessions
- CI: GitHub Actions

## 4. Actors
- Guest: A user who is not logged in
- User: A registered and authenticated user

## 5. Functional Specifications

### 5.1 Authentication
- The system shall allow guests to register using email and password.
- The system shall validate password confirmation during signup.
- The system shall prevent duplicate email registration.
- The system shall authenticate users using hashed passwords.
- The system shall maintain user sessions after login.
- The system shall allow users to log out and clear the session.

### 5.2 Dashboard Access
- The dashboard shall be accessible only to authenticated users.
- Unauthorized users attempting to access the dashboard shall be redirected to login.

### 5.3 Task Management
- The system shall allow users to create new tasks.
- Each task shall include:
  - ID
  - Title
  - Description
  - Status (Pending, In Progress, Completed)
  - Assigned user
- The system shall allow users to edit existing tasks.
- The system shall allow users to delete tasks.
- The system shall display only tasks assigned to the logged-in user.

### 5.4 Task Search and Organization
- The system shall allow users to search tasks by title or description.
- The system shall allow users to filter tasks by status.
- The system shall allow users to sort tasks by title or status.

## 6. Non-Functional Specifications
- Passwords shall be stored securely using hashing.
- The system shall provide clear success and error messages.
- The user interface shall be accessible through modern web browsers.
- The system shall be simple, responsive, and easy to use.
- Automated unit tests shall be executed using GitHub Actions CI.

## 7. Constraints
- No external database is used (JSON files only).
- The system runs locally using Flask.
- Authentication is session-based.

## 8. Assumptions
- Users access the system via a web browser.
- The number of users and tasks is small (academic project scope).

## 9. Future Enhancements
- Replace JSON storage with a database.
- Add role-based access control.
- Add task deadlines and priorities.
- Deploy the system to a cloud platform.
