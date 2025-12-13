
### C) `diagrams/class-diagram.md`
classDiagram
  class User {
    +email: string
    +password_hash: string
  }

  class Task {
    +id: int
    +title: string
    +description: string
    +assigned_to: string
    +status: string
  }

  class FlaskApp {
    +signup()
    +login()
    +dashboard()
    +logout()
    +me()
    +get_tasks()
    +add_task()
    +edit_task()
    +delete_task()
    +load_users()
    +save_users()
    +load_tasks()
    +save_tasks()
  }

  FlaskApp --> User : reads/writes
  FlaskApp --> Task : reads/writes
