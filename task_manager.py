# Importing the datetime module to use to compare dates later on in the code i.e. to tell if a task managed is overdue.
import datetime
from datetime import datetime

        
# Define functions to be used in the program.
# Function 1: reg_user is called when the user selects 'r' to register a user.
def reg_user(menu_choice):
    
    #Setting the if statement for menu_choice.
    if menu_choice == "r":

        new_user = input("Please enter a new username: \n")

        # Checking if the username already exists in the usernames_list.
        # Whilst listed, the user is prompted to re-enter a new username and an error message is displayed.
        while new_user in usernames_list:

            print("The username you entered is already listed.")

            new_user = input("Please enter a new username: \n")
   
        # If the new username is not already listed, it is added to usernames_list.
        # The updated list is then updated in the dictionary user_details.
        if new_user not in usernames_list:

            usernames_list.append(new_user)

            user_details["Usernames"] = usernames_list  
                 
        new_password = input("Please enter a new password: \n")

        pass_confirm = input("Please confirm your new password: \n")        

        # If the new and confirmed password values do not match, an appropriate error message is displayed.
        # The user is then prompted to enter their new password and confirm it until they match.
        while new_password != pass_confirm:

            print("Your confimed password does not match the original password.")
            new_password = input("Please enter your new password: \n")
            pass_confirm = input("Please confirm your new password: \n") 
            
        # If the new and confirmed password values match, a successful message is displayed.
        # The new password is added to the passwords_list.
        if new_password == pass_confirm:
            passwords_list.append(new_password)  
            user_details["Passwords"] = passwords_list  

            # user.txt file opened to write to.
            with open('user.txt', 'a+') as f:
                # Using for statement to print username and passwords on separate lines.
                # The number of lines is equal to the number of items in usernames_list.
                for i in range(len(usernames_list)):
                        # Writing from the apppropriate dictionary keys, in the correct format. 
                        f.write(user_details["Usernames"][i] + ", " + user_details["Passwords"][i] + '\n')
                        
        # Message returned at the end of function.
        return("Your new username and password have been successfully added.")
        

# Function 2: add_task is called when a user selects 'a' to add a new task. 
def add_task(menu_choice):

    if menu_choice == "a":

        import datetime
        from datetime import date

        # Getting user input on the username of the person the task is assigned to.
        name = input("Please enter the username of the person you wish to assign the task to: \n")
        
        # Getting user input on the title of the task being added. 
        title = input("Please enter the title of the task: \n")
        
        # Getting information regarding the description of the added task.
        descrip = input("Please enter a description of the task: \n")

        # Using the previously imported datetime module today() function to calculate the current date.
        current_date = datetime.date.today()

        # Changing the date object to a string in the correct date format.
        assigned_date = current_date.strftime('%d %b %Y')

        # Getting input on the due date of the task being added.
        date_format = input("Please enter the due date of the task (e.g. dd-mm-yyyy): \n")

        date_list = date_format.split("-")

        numbers_date = [int(x) for x in date_list]

        due_date = date(numbers_date[2], numbers_date[1], numbers_date[0]).strftime('%d %b %Y') 

        # task_completed is automatically set to "No" when adding a new task. 
        task_completed = "No"

        # Casting all the user input info into a list, to add to the tasks_dict.
        task_list = [name, title, descrip, assigned_date, due_date, task_completed]

        tasks_dict[f"Task {count} details:"] = task_list    

        # Opening the tasks.txt file to enter the new task information.
        with open('tasks.txt', 'r+') as f2:

            # Printing the list values for each key in tasks_dict to a new line.
            for key in tasks_dict:
                # Casting to a string enabling the info to be written to the file.
                line_string = str(tasks_dict[key])  

                bad_chars = ["[", "]", "\'",]
                # Taking out characters pertaining to previous list/dictionary format.
                for i in bad_chars:  
                    line_string = line_string.replace(i, "")
                # Writing the correct format of each string line to the file.
                f2.write(line_string + '\n')   

        # Message returned at the end of the function. 
        return("Your new task has been added successfully.")

# Function 3: view_all is called when a user selects 'va' to view all tasks listed in tasks.txt.
# These tasks are already stored in the dictionary 'tasks_dict'.
# Therefore, the dictionary will be used to view all the tasks.
def view_all(menu_choice):

    if menu_choice == "va":

        task_count = 0

        for key in tasks_dict:

            task_count += 1

            print(f"""____________________________________________
Task {str(task_count)}:     {str(tasks_dict[key][1])}
Assigned to:            {str(tasks_dict[key][0])}
Date assigned:          {str(tasks_dict[key][3])}
Due Date:               {str(tasks_dict[key][4])}
Task Complete?          {str(tasks_dict[key][5])}
Task Description:
 {str(tasks_dict[key][2])}
________________________________________________""")

    return("End of Tasks.")

# Function 4: view_mine is called when a user selects 'vm' to view all tasks assigned to them.
def view_mine(menu_choice, username):

    if menu_choice == "vm":

        task_count = 0

        for key in tasks_dict:
            # calculating the total number of tasks by increasing the count through tasks_dict.
            task_count += 1
            # If the task is assigned to the user, it is displayed.
            if username == (tasks_dict[key][0]):  

                print(f"""
Task {str(task_count)}:      \t{str(tasks_dict[key][1])}
Assigned to:        {str(tasks_dict[key][0])}
Date assigned:      {str(tasks_dict[key][3])}
Due Date:           {str(tasks_dict[key][4])}
Task Complete?      {str(tasks_dict[key][5])}
Task Description:
 {str(tasks_dict[key][2])}
\n""")  # This is a user friendly format with numbered tasks.


        return("End of Tasks. \n")        
            

# Function 5: Generating text files 'task_overview.txt' and 'user_overview.txt'.
# I made this a function because it is needed twice in the menu, for 'display statistics'.
# I did not want to repeat the code, so therefore a function was needed.
def display_statistics():

    task_overview = ""  
    user_overview = ""

    f3 = open ("task_overview.txt", 'w')

    # Total number of tasks is equal to the key count of tasks_dict.
    tasks_total = len(tasks_dict)
    #Setting variables for integers concerning complete tasks, incomplete tasks and overdue tasks respectively.
    x = 0   
    y = 0

    for key in tasks_dict:

        if tasks_dict[key][5] == "Yes":  
            x += 1  

        elif tasks_dict[key][5] == "No":
            y += 1  

    # Adding a string with the total tasks number to the task_overview string. 
    task_overview = print("The total number of tasks is " + str(x+y))

    # Now generating a 'user_overview' file.
    # The user_overview string is then written to the file in an easy to read format.
    user_overview = " "
    count = 0
    with open('user.txt', 'r') as f4:
        for line in f4:
            if line.strip():
                count += 1
         
    # Writing all the info calculated above into sentence strings which are built into the user_overview string variable.
    user_overview = print("The total number of users registered is {}".format(count))


    # The user then views a message stating that their reports have been successfully generated.
    # They do not have the option to view the reports.
    # The admin user can select to display statistics from their main menu.
    return("Your statistics have been generated successfully: \n")

# In the first version of this code, I used a string to store the user and task contents.
# Now, the user and tasks details will be stored in corresponding dictionaries for use in the program.
user_details = {}

# The user details dictionary will be built with lists from 'usernames_list' and 'passwords_list' as values.
usernames_list = []
passwords_list = []
login_list = []
tasks_dict = {}

# Opening the tasks.txt file to read and write information from it.
# Adding the info in the user.txt file into the set list.
with open('user.txt') as textfile:

    for line in textfile.readlines():

        codes = line.split(', ')
        user_details[codes[0]] = codes[1].strip()
print('Please log in')
while True:
    username = input('Please enter your name: ')
    p = input('Enter your password: ')
    if (password := user_details.get(username)) and password == p:
        break
    print('Incorrect username or password')
print('You are successfully logged in. \n')

# Setting a count to keep track of the number of lines in the tasks.txt file.
count = 1

# Opening the tasks.txt file to read and write information to it.
with open('tasks.txt', 'r+') as f2:

    for line in f2:        
        newline = line.rstrip('\n')          
        split_line = newline.split(", ")  
        tasks_dict[f"Task {count} details:"] = split_line 
        count += 1  # Count used to change key value for each list of info.

# Indefinite loop created to display the menu once the user is logged in.
# This allows the user to return to the menu after each option.
# If they wish to exit the program, they can choose the 'exit' option from the menu. 
while 1:
    # The admin user views a specific menu.
    if username == "admin":  
        
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
ds - display statistics
e - Exit
: ''').lower()

    else:  #All other users can only view this menu.

       menu = input('''Select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

    if menu == 'r':
        print(reg_user(menu))

    elif menu == 'a':
        print(add_task(menu))
        
    elif menu == 'va':
        print(view_all(menu))

    elif menu == 'vm':
        print(view_mine(menu, username))

    elif menu == 'ds':
        print(display_statistics())  
    

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again \n")
