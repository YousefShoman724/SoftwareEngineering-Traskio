sequenceDiagram
  actor U as User
  participant B as Browser
  participant S as Flask Server
  participant F as backend/users.json

  U->>B: Enter email & password
  B->>S: POST /login
  S->>F: load_users()
  F-->>S: users list

  alt Valid credentials
    S->>S: create session
    S-->>B: Redirect to /dashboard
    B->>S: GET /dashboard
    S->>S: check active session
    S-->>B: Render dashboard.html
  else Invalid credentials
    S-->>B: Redirect to /login with error message
  end
