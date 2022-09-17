# Level-1-Capstone-Project-2

This program is designed for small businesses, to assist with task management for each member of a team.

task.manager.py works with two text files:
1 - users.txt - stores the username and password for each userthat has permission to use the program.
2 - tasks.txt - stores a list of all the tasks that a team is working on. The data for each task is stored on a separate line in this text file. Each line includes the                   following data about a task in the following order:
                - the username of the person to whom the task is assigned
                - the title of the task
                - a description of the task
                - the date that the task was assigned to the user
                - the due date for the task
                - a "Yes" or "No" value that specifies if the task has been completed yet
               
This program allows the users to login. The user will be prompted to enter a username and password.

An error message will be displayed if the user enters a username that is not listed in the 'user.txt' file, and the user will be prompted repeatedly to enter a valid username and password until they provide appropriate credentials.

The following menu will be displayed once the user successfully logs in:
- 'r' - register user
- 'a' - add task
- 'va' - view all tasks
- 'vm' - view my tasks
- 'e' - exit

If the user chooses 'r' to register a user, the user will be prompted for a new username and password. The user will also be asked to confirm the password. If the value entered to confirm the password matches the value of the password, the username and password will be written to the user.txt file.

If the user chooses 'a' to add a task, the user will be promted to enter:
- the username of the person the task is assigned to
- the title of the task
- a description of the task
-  the due date of the task
The data about the new task will be written to the tasks.txt file.

If the user chooses 'va' to view all tasks, the information for each task will be displayed.

If the user chooses 'vm' to view the tasks that are assigned to them, only the tasks that have been assigned to the user that is currently logged-in, will be displayed.

Only the user with the username 'admin' is allowed to register users.

The admin user is provided with an extra menu option that allows them to display statistics, which displays the total number of tasks and the total number of users.
