flowchart LR
  Guest([Guest]) --> UC1((Sign Up))
  Guest([Guest]) --> UC2((Log In))
  User([User]) --> UC3((View Dashboard))
  User([User]) --> UC4((Log Out))
  User([User]) --> UC5((Add Task))
  User([User]) --> UC6((Edit Task))
  User([User]) --> UC7((Delete Task))
  User([User]) --> UC8((Assign Task))
  User([User]) --> UC9((View Task List))
  User([User]) --> UC10((View Users))

  UC3 --> P1[[Requires Session]]
  UC4 --> P1
  UC5 --> P1
  UC6 --> P1
  UC7 --> P1
  UC8 --> P1
  UC9 --> P1
  UC10 --> P1
