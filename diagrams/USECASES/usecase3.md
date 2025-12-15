
### C) `diagrams/class-diagram.md`
classDiagram
  class User {
    +email: string
    +password_hash: string
  }

  class SubTask {
    +id: int
    +title: string
    +completed: boolean
  }

  class Task {
    +id: int
    +title: string
    +description: string
    +assigned_to: string
    +status: string
    +deadline: string
    +subtasks: list<SubTask>
  }

  class FlaskApp {
    +signup()
    +login()
    +logout()
    +dashboard()
    +check_session()

    +get_tasks()
    +add_task()
    +edit_task()
    +delete_task()

    +add_subtask()
    +update_subtask_status()

    +search_tasks()
    +filter_tasks()

    +load_users()
    +save_users()
    +load_tasks()
    +save_tasks()
  }

  FlaskApp --> User : reads/writes
  FlaskApp --> Task : reads/writes
  Task --> SubTask : contains
