# Traskio – Use Case Specifications

## Actor
- **User**: Any registered user of the system.

---

## UC-01: User Registration (Sign Up)

**Actor:** User  

**Description:**  
Allows a new user to create an account by providing an email and password.

**Preconditions:**
- User is not logged in.
- Email does not already exist in the system.

**Main Flow:**
1. User opens the signup page.
2. User enters email, password, and confirm password.
3. System validates the input.
4. System saves the user in `users.json`.
5. System displays a success message.

**Alternative Flow:**
- Email already exists → system displays an error.
- Passwords do not match → system displays an error.

**Postconditions:**
- New user account is created.

---
