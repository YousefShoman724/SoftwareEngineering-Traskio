# Manual Test Cases — Traskio Phase 2

| ID | Title | Preconditions | Steps | Expected Result |
|----|-------|---------------|-------|-----------------|
| TC-01 | Signup – Successful registration | Application is running | Open /signup_page, enter a valid email and matching passwords, click Sign Up | User is registered successfully and receives a success message |
| TC-02 | Signup – Duplicate email | Email already exists in system | Open signup page, enter an existing email, submit form | Registration is rejected with an error message |
| TC-03 | Signup – Password mismatch | Application is running | Enter password and different confirm password, submit | Registration is rejected with password mismatch error |
| TC-04 | Login – Successful login | User account exists | Open login page, enter valid email and password, submit | User is logged in and redirected to dashboard |
| TC-05 | Login – Invalid credentials | User account exists | Enter valid email with wrong password, submit | Login fails and error message is shown |
| TC-06 | Dashboard – Access without login | User not logged in | Manually navigate to /dashboard | User is redirected to login page |
| TC-07 | Dashboard – Access after login | User is logged in | Login successfully then open /dashboard | Dashboard page loads successfully |
| TC-08 | Logout | User is logged in | Click logout button then try to access /dashboard | Session is cleared and user is redirected to login page |
| TC-09 | Add Task – Successful | User is logged in | Enter task title and details, click Add Task | Task is added and appears in task list |
| TC-10 | Add Task – Missing title | User is logged in | Leave title empty and submit task | Task creation is rejected with error message |
| TC-11 | Edit Task | Task exists | Click Edit, modify task data, click Update | Task details are updated successfully |
| TC-12 | Delete Task | Task exists | Click Delete on a task | Task is removed from the list |
| TC-13 | Filter Tasks by Status | Multiple tasks exist | Select a status filter and apply | Only tasks with selected status are displayed |
| TC-14 | Search Tasks | Tasks exist | Enter keyword in search box | Matching tasks are displayed |
| TC-15 | Sort Tasks | Multiple tasks exist | Click sort by title or status | Tasks are displayed in sorted order |
