# Traskio Project Backlog

| ID   | User Story / Task Description                                                      | Feature / Module        | Priority |
|------|----------------------------------------------------------------------------------|------------------------|----------|
| US01 | User can sign up with email and password                                          | Authentication         | High     |
| US02 | User can log in with email and password                                           | Authentication         | High     |
| US03 | User can log out from the system                                                  | Authentication         | High     |
| US04 | User can create a new task with title, description, priority, and optional deadline | Task Management      | High     |
| US05 | User can edit existing tasks                                                      | Task Management        | High     |
| US06 | User can delete tasks                                                             | Task Management        | High     |
| US07 | User can view task details including subtasks, comments, and tags                | Task Management        | High     |
| US08 | User can add and manage subtasks under a main task                                | Task Management        | Medium   |
| US09 | User can add, view, and edit comments on tasks                                    | Task Management        | Medium   |
| US10 | User can add and manage tags for tasks                                            | Task Management        | Medium   |
| US11 | User can start/stop time tracking for each task                                    | Time Tracking          | Medium   |
| US12 | Dashboard displays task statistics (total, pending, completed)                    | Dashboard              | High     |
| US13 | Dashboard accessible only to authenticated users                                  | Dashboard              | High     |
| US14 | System validates user input (email format, password strength)                     | Authentication         | High     |
| US15 | System prevents duplicate emails during signup                                     | Authentication         | High     |
| US16 | System stores passwords securely using hashing                                     | Authentication         | High     |
| US17 | System provides clear error messages for invalid inputs                            | Authentication/Task Management | Medium |
| US18 | User can assign tasks to themselves or others (if multi-user support exists)      | Task Management        | Medium   |
| US19 | System allows marking tasks as complete                                           | Task Management        | High     |
| US20 | User can filter and search tasks by status, tags, or deadline                     | Task Management        | Medium   |
| US21 | System auto-saves task changes                                                    | Task Management        | Medium   |
| US22 | Backend provides RESTful API endpoints for all CRUD operations                     | API Layer              | High     |
| US23 | System ensures data integrity and consistency in JSON storage                      | Storage Management     | High     |
| US24 | Frontend displays tasks in a user-friendly and intuitive interface                 | Frontend Components    | High     |
| US25 | System tracks total time spent on each task                                        | Time Tracking          | Medium   |
| US26 | Users can view a summary of tasks by priority or status                             | Dashboard              | Medium   |
| US27 | System restricts access to pages for unauthenticated users                         | Security               | High     |
| US28 | System runs locally at http://127.0.0.1:5000                                       | System Constraints     | Medium   |
| US29 | Backend modular design allows future migration to relational database              | Maintainability/Scalability | Medium |
| US30 | System provides clear notifications for task deadlines                              | Task Management        | Medium   |
| US31 | User can reset their password via email link (if implemented)                       | Authentication         | Low      |
| US32 | System logs user activity for auditing purposes                                    | Security               | Low      |
| US33 | System is compatible with modern browsers                                         | Frontend Components    | Medium   |
| US34 | User interface responsive for mobile and desktop devices                           | Frontend Components    | High     |
| US35 | System provides visual indicators for overdue tasks                                 | Dashboard/Task Management | Medium |
| US36 | Users can customize task priority levels                                           | Task Management        | Medium   |
| US37 | API validates all incoming requests and returns proper HTTP status codes           | API Layer              | High     |
| US38 | System allows future addition of collaborative tasks                               | Scalability/Task Management | Medium |
| US39 | Frontend uses reusable components for task forms, lists, and details              | Frontend Components    | Medium   |
| US40 | System supports time zone adjustments for deadlines (optional)                     | Task Management        | Low      |
