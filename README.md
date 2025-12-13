# Traskio - Task Management Application (Beta)

Traskio is a task management application that helps users organize, manage, and track their tasks efficiently. The system allows users to sign up, log in, and manage tasks through a protected dashboard.

## Overview

Traskio provides a simple and effective way to manage tasks. Users can create, edit, delete, assign, and track tasks with different statuses such as Pending, In Progress, and Completed. Access to the dashboard is restricted to authenticated users only.

## Key Features

- User signup and login  
- Secure password handling (hashed passwords)  
- Protected dashboard (login required)  
- Add, edit, delete, and assign tasks  
- View task list with status tracking  
- Task status categories: Pending, In Progress, Completed  
- Search and filter tasks  
- User logout with session clearing  
- Automated unit testing  
- Continuous Integration using GitHub Actions  

## Tools and Technologies

- Backend: Python (Flask)  
- Frontend: HTML, CSS, JavaScript  
- Data Storage: users.json for user accounts, tasks.json for task data  
- Testing: Python unittest  
- CI/CD: GitHub Actions  

## Project Structure

SoftwareEngineering-Traskio/
├── backend/
│   ├── main.py
│   ├── users.json
│   └── tasks.json
├── frontend/
│   └── .gitkeep
├── diagrams/
│   ├── SequenceDiagram.txt
│   └── ClassDiagram.txt
├── docs/
│   ├── requirements.md
│   ├── specifications.md
│   ├── test-cases.md
│   └── scrum/
│       └── 2025-12-12.md
├── tests/
│   └── test_main.py
├── README.md
└── requirements.txt

## How to Run Locally

1. Clone the repository  
git clone https://github.com/your-repo/Traskio.git  

2. Navigate to the project directory  
cd TraskioPhase2/SoftwareEngineering-Traskio  

3. Create a virtual environment  
python -m venv venv  

4. Activate the virtual environment  
Windows CMD: venv\Scripts\activate.bat  
PowerShell: Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass; venv\Scripts\Activate.ps1  

5. Install dependencies  
pip install -r requirements.txt  

6. Run the application  
python backend/main.py  

Open your browser and go to http://127.0.0.1:5000/

## Testing

To run unit tests:  
python -m unittest discover tests  

The tests cover user signup, user login, invalid login attempts, dashboard access control, and session handling.

## Documentation

Requirements: docs/requirements.md  
Specifications: docs/specifications.md  
Test Cases: docs/test-cases.md  
Scrum Meetings: docs/scrum/  
Diagrams: Use Case, Sequence Diagram, Class Diagram, Deployment Diagram  

## Author

Developed by: 
**Yousef Wael Shoman**
**Mariam Mohamed Behairy**

