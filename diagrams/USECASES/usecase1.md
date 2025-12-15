flowchart LR
  Guest([Guest]) --> UC1((Sign Up))
  Guest([Guest]) --> UC2((Log In))

  User([Authenticated User]) --> UC3((View Dashboard))
  User --> UC4((Log Out))

  User --> UC5((Add Task))
  User --> UC6((Edit Task))
  User --> UC7((Delete Task))
  User --> UC8((Assign Task))
  User --> UC9((View Task List))

  User --> UC11((Add Sub-Task))
  User --> UC12((Update Sub-Task Status))
  User --> UC13((View Task Progress))
  User --> UC14((Set Deadline))
  User --> UC15((Search Tasks))
  User --> UC16((Filter Tasks by Status))

  UC3 --> P1[[Requires Active Session]]
  UC4 --> P1
  UC5 --> P1
  UC6 --> P1
  UC7 --> P1
  UC8 --> P1
  UC9 --> P1
  UC11 --> P1
  UC12 --> P1
  UC13 --> P1
  UC14 --> P1
  UC15 --> P1
  UC16 --> P1
