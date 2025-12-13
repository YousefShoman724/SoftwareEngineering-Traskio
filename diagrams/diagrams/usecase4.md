
### D) `diagrams/deployment.md`
flowchart TB
  U[User Browser] -->|HTTP| APP[Flask App]
  APP -->|reads/writes| JS[(users.json)]
  APP -->|reads/writes| TS[(tasks.json)]
  APP -->|serves files| FE[Frontend (HTML/CSS/JS)]
  U -->|views pages| FE
