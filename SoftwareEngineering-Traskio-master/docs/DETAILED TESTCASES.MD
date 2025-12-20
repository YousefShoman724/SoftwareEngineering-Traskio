# Test Cases — Traskio Task Management System

## Overview
This document defines the test cases for the Traskio application.  
The test cases cover authentication, authorization, and task management features based on the implemented Flask backend and frontend UI.

---

## Actors
- Guest (Not logged in)
- Authenticated User (Logged in)

---

## Authentication Test Cases

### TC-01: Successful User Signup
**Actor:** Guest  
**Precondition:** User is not registered  
**Steps:**
1. Open Signup page
2. Enter a valid email
3. Enter a password
4. Enter the same password in confirm password
5. Click "Create Account"

**Expected Result:**
- Account is created successfully
- Success message is displayed
- User is redirected to Login page

---

### TC-02: Signup with Existing Email
**Actor:** Guest  
**Precondition:** Email already exists in users.json  
**Steps:**
1. Open Signup page
2. Enter an already registered email
3. Enter password and confirm password
4. Click "Create Account"

**Expected Result:**
- Signup is rejected
- Error message "Email already exists" is displayed

---

### TC-03: Signup with Mismatched Passwords
**Actor:** Guest  
**Steps:**
1. Open Signup page
2. Enter email
3. Enter password
4. Enter different confirm password
5. Click "Create Account"

**Expected Result:**
- Signup is rejected
- Error message "Passwords do not match" is displayed

---

### TC-04: Successful Login
**Actor:** Guest  
**Precondition:** User account exists  
**Steps:**
1. Open Login page
2. Enter valid email
3. Enter correct password
4. Click "Sign In"

**Expected Result:**
- Login succeeds
- Session is created
- User is redirected to Dashboard

---

### TC-05: Login with Invalid Credentials
**Actor:** Guest  
**Steps:**
1. Open Login page
2. Enter invalid email or password
3. Click "Sign In"

**Expected Result:**
- Login fails
- Error message "Invalid email or password" is displayed

---

### TC-06: Access Dashboard Without Login
**Actor:** Guest  
**Steps:**
1. Directly access `/dashboard` URL

**Expected Result:**
- Access is denied
- User is redirected to Login page

---

### TC-07: Logout
**Actor:** Authenticated User  
**Precondition:** User is logged in  
**Steps:**
1. Click Logout

**Expected Result:**
- Session is cleared
- User is redirected to Login page

---

## Task Management Test Cases

### TC-08: Add New Task
**Actor:** Authenticated User  
**Steps:**
1. Open Dashboard
2. Enter task title
3. Enter task details
4. Click Add Task

**Expected Result:**
- Task is saved in tasks.json
- Task appears in task list

---

### TC-09: View User Tasks
**Actor:** Authenticated User  
**Precondition:** User has tasks  
**Steps:**
1. Open Dashboard

**Expected Result:**
- Only tasks assigned to logged-in user are displayed

---

### TC-10: Edit Existing Task
**Actor:** Authenticated User  
**Precondition:** Task exists  
**Steps:**
1. Click Edit on a task
2. Modify task fields
3. Save changes

**Expected Result:**
- Task data is updated successfully

---

### TC-11: Delete Task
**Actor:** Authenticated User  
**Precondition:** Task exists  
**Steps:**
1. Click Delete on a task

**Expected Result:**
- Task is removed from tasks.json
- Task disappears from UI

---

### TC-12: Unauthorized Task Access
**Actor:** Guest  
**Steps:**
1. Send request to `/tasks` API without login

**Expected Result:**
- Request is rejected
- HTTP status 401 is returned

---

## Automated Testing

### TC-13: Run Unit Tests
**Tool:** unittest / pytest  
**Steps:**
1. Run `python test_main.py`

**Expected Result:**
- All tests pass successfully
- Authentication logic is validated

---

## Notes
- Passwords are stored hashed using Werkzeug
- Sessions are managed using Flask sessions
- Test cases align with implemented backend routes and frontend behavior
