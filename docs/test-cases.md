# Test Cases Documentation

## 1. User Authentication – Login

| Test Case ID | Title | Precondition | Steps | Expected Result |
|-------------|-------|--------------|-------|-----------------|
| TC-LOGIN-01 | Login with valid credentials | User is registered | 1. Open login page<br>2. Enter valid email<br>3. Enter valid password<br>4. Click Login | User is redirected to dashboard |
| TC-LOGIN-02 | Login with invalid password | User is registered | 1. Open login page<br>2. Enter valid email<br>3. Enter wrong password<br>4. Click Login | Error message is displayed |
| TC-LOGIN-03 | Login with empty fields | None | 1. Open login page<br>2. Click Login without entering data | Validation message appears |

---

## 2. User Authentication – Sign Up

| Test Case ID | Title | Precondition | Steps | Expected Result |
|-------------|-------|--------------|-------|-----------------|
| TC-SIGNUP-01 | Sign up with valid data | Email not registered | 1. Open signup page<br>2. Fill all fields correctly<br>3. Click Sign Up | Account created successfully |
| TC-SIGNUP-02 | Sign up with existing email | Email already exists | 1. Open signup page<br>2. Enter existing email<br>3. Click Sign Up | Error message appears |
| TC-SIGNUP-03 | Sign up with empty fields | None | 1. Open signup page<br>2. Click Sign Up | Validation messages appear |

---

## 3. Task Management

| Test Case ID | Title | Precondition | Steps | Expected Result |
|-------------|-------|--------------|-------|-----------------|
| TC-TASK-01 | Add new task | User logged in | 1. Open dashboard<br>2. Click Add Task<br>3. Enter task details<br>4. Save | Task appears in task list |
| TC-TASK-02 | Edit task | Task exists | 1. Select task<br>2. Click Edit<br>3. Update data<br>4. Save | Task updated successfully |
| TC-TASK-03 | Delete task | Task exists | 1. Select task<br>2. Click Delete | Task removed from list |

---

## 4. API Endpoint Tests

| Test Case ID | Endpoint | Method | Input | Expected Result |
|-------------|----------|--------|-------|-----------------|
| TC-API-01 | /login | POST | Valid credentials | Status 200 – Success |
| TC-API-02 | /login | POST | Invalid credentials | Status 401 – Unauthorized |
| TC-API-03 | /tasks | GET | Auth token | Status 200 – Tasks returned |

---

## 5. Permissions & Security

| Test Case ID | Title | Precondition | Steps | Expected Result |
|-------------|-------|--------------|-------|-----------------|
| TC-SEC-01 | Access dashboard without login | User not logged in | 1. Open dashboard URL | Redirected to login |
| TC-SEC-02 | Access API without token | None | 1. Call API without token | Status 403 – Forbidden |

---

**End of Test Cases**
