## UC-02: User Login

**Actor:** User  

**Description:**  
Allows a registered user to log in to the system.

**Preconditions:**
- User has a valid account.
- User is not logged in.

**Main Flow:**
1. User opens the login page.
2. User enters email and password.
3. System validates credentials.
4. System creates a session.
5. User is redirected to the dashboard.

**Alternative Flow:**
- Invalid credentials → system displays an error message.

**Postconditions:**
- User session is active.

---
