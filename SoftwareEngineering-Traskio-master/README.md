# Traskio - Task Management Application

Traskio is a modern task management application that helps users organize, manage, and track their tasks efficiently. The system provides a secure and interactive dashboard with real-time updates, sub-task support, and dynamic progress tracking.

## Overview

Traskio offers a simple yet powerful way to manage daily tasks. Users can sign up, log in, and access a protected dashboard where they can create, edit, delete, and assign tasks. Each task can include sub-tasks, deadlines, and status tracking (Pending, In Progress, Completed). All sensitive areas are restricted to authenticated users only.


### User Management
- User signup and login
- Secure password hashing
- Password strength indicator during signup
- Session-based authentication
- Protected dashboard (login required)
- User logout with session clearing


### Task Management
- Add, edit, delete, and assign tasks
- Sub-tasks with individual completion tracking
- Dynamic progress bars based on sub-task completion
- Task deadlines with automatic sorting
- Task status categories: Pending, In Progress, Completed
- Color-coded task cards based on status
- Search and filter tasks by title, description, and status
- Real-time updates without page refresh

### UI / UX
- Modern and clean user interface
- Glassmorphism design with smooth animations
- Fully responsive design (desktop, tablet, mobile)

### Development & Quality
- Automated unit testing using Python `unittest`
- Continuous Integration using GitHub Actions
- Clear project structure following software engineering best practices


## Tools and Technologies

- Backend: Python (Flask)
- Frontend: HTML, CSS, JavaScript
- Data Storage:
  - `backend/users.json` for user accounts
  - `backend/tasks.json` for tasks data
- Testing: Python `unittest`
- CI/CD: GitHub Actions



## How to Run Locally

1. Clone the repository  
```
git clone https://github.com/your-repo/Traskio.git
```

2. Navigate to the project directory  
```
cd TraskioPhase2/SoftwareEngineering-Traskio
```

3. Create a virtual environment  
```
python -m venv venv
```

4. Activate the virtual environment  
```
Windows CMD: venv\Scripts\activate.bat
PowerShell: Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass; venv\Scripts\Activate.ps1
```

5. Install dependencies  
```
pip install -r requirements.txt
```

6. Run the application  
```
python backend/main.py
```

Open your browser and go to http://127.0.0.1:5000/

## Documentation

- Requirements: `docs/requirements.md`
- Specifications: `docs/specifications.md`
- Test Cases: `docs/test-cases.md`
- Scrum Meetings: `docs/scrum/`
- Diagrams:
  - Use Case Diagram
  - Sequence Diagram
  - Class Diagram
  - Deployment Diagram

## Author

Developed by:  
**Yousef Wael Shoman**  
**Mariam Mohamed Behairy**
