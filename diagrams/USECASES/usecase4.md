
### D) `diagrams/deployment.md`
flowchart TB
  U[User Browser]

  FE[Frontend<br/>(HTML / CSS / JavaScript)]
  APP[Flask Application<br/>(backend/main.py)]
  UDB[(backend/users.json)]
  TDB[(backend/tasks.json)]

  U -->|HTTP Requests| APP
  APP -->|Serves Pages & APIs| FE
  FE -->|Rendered UI| U

  APP -->|Read / Write| UDB
  APP -->|Read / Write| TDB

