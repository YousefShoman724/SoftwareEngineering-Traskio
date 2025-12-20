# Scrum Meeting Summary 
## Attendees
- Mariam Mohamed Behairy
- Yousef wael Shoman

## Agenda
- Review authentication implementation in `main.py`
- Review frontend pages (login.html, signup.html, dashboard.html)
- Review task CRUD APIs and data storage
- Review unit testing setup
- Review CI status (GitHub Actions)

## What was done
- Implemented user authentication (Signup & Login) using Flask sessions in `main.py`
- Added password hashing using `werkzeug.security`
- Implemented protected routes for Dashboard access
- Implemented task management APIs:
  - Add task
  - Edit task
  - Delete task
  - View tasks assigned to logged-in user
- Connected frontend (HTML/JS) with backend APIs using `fetch`
- Stored users and tasks data in JSON files (`users.json`, `tasks.json`)
- Added file permission handling using `fix_permissions.py`
- Implemented unit tests for authentication using `unittest` in `test_main.py`
- Verified that dashboard access is restricted to authenticated users
- Updated README with project overview, tools, and run instructions

## Blockers
- None

## Action Items
- Finalize documentation for Phase 2 submission
- Ensure diagrams and test cases are included in the repository
- Perform final review of GitHub repository structure
- Submit Phase 2 deliverables
