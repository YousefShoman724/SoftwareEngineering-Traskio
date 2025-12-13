sequenceDiagram
  actor U as User
  participant B as Browser
  participant S as Flask Server
  participant F as users.json

  U->>B: Enter email & password
  B->>S: POST /login
  S->>F: load_users()
  F-->>S: users list
  alt valid credentials
    S-->>B: Login successful, Redirect /dashboard
    B->>S: GET /dashboard
    S-->>B: dashboard.html
  else invalid credentials
    S-->>B: Login failed, Redirect /
  end
