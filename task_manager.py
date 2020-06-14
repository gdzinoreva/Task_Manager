#This is a program for a small business that helps it to manage tasks assigned to each member of the team.
#The user must login at the beginning of the progam.
#The list of valid users that the program uses is stored in a text file and tasks in a separate text file.
#Once user successfully logs in a menu option is provided and user is prompted to select from the menu and results produced accordingly.
#If the user is an 'admin' then there is an additional menu available for them.


import datetime                     #imports the datetime library module
from datetime import date           #gets the 'date' class




#This section defines the functions that the rest of the program will use.

def menu_options():                 #menu options print function
    print()
    print("Ordinary Menu, please select one of the following options:")
    print("\tr   - register user")
    print("\ta   - add task")
    print("\tva  - view all tasks")
    print("\tvm  - view my tasks")
    print("\tgr  - generate reports")
    print("\te   - exit")
    print()




def reg_user():                     #funtion to register a new user
    print("\nYou have selected to Register a New User.\n")       #displays info
    with open('user.txt', 'r', encoding='utf-8') as user_file:            #opens user file in append mode
        username_new = input("Enter a new username register a new user: ")          #gets username input from user

        user_new = False
        username_list = []                          #generates list of usernames
        for line in user_file:                      #loop for string manipulation of text file
            line = line.split(",")
            user = line[0]
            username_list.append(line[0])

        while user in username_list:                #if a username already exists ask for another one
            if username_new not in username_list:   #if username does not exist carry on with program
                break
            elif user in username_list:
                print("username already exists!")
                username_new = input("Enter a new username register a new user: ")
                      
        password_new = input("Enter the password: ")                #gets password input from user
        confirm = input("Confirm password: ")                       #gets password again

    with open('user.txt', 'a', encoding='utf-8') as user_file:        #opens file in append mode
        if password_new == confirm:                                 #cheks if inputs match
            new = f"\n{username_new}, {password_new}"                 #format required for user file     
            user_file.write(new)                                    #writes infomation to user file in format above
            print("\nSuccessfully added new user")#displays message
        else:
            print("\nUnable to register new user. Passwords do not match.")       #error message if password inputs do not match
                
        if ordinary_option == "r" and logged_user != "admin":
            print("Only admin is allowed to register a new user! Please login as admin.")    #error message if user is not an admin and selects this option




def add_task():                                 #defines function to add a new task
    print("\nYou have selected to Add New Task.\n")
    with open('tasks.txt', 'a', encoding='utf-8') as task_file:           #opens tasks file in append mode       
        j = 0
        tasks = int(input("\nPlease enter the number of tasks you would like to add: "))        #gets number of tasks to be added to act as range
        for j in range (tasks):
            user = input("\nEnter user you are assigning task to: ")              #gets task information to assign
            title = input("Enter title of task: ")
            description = input("Enter the task discription: ")
            assign_date = date.today()                  #uses datetime module to generate today's date
            due_date = input("Enter due date of task, format dd Month YYYY: ")

            new_task = f"\n{user}, {title}, {description}, {due_date}, {assign_date.strftime('%d %B %Y')}, No"       #all information to be written
            task_file.write(new_task)                   #writes to task file
        print("\nYou have successfully added task(s).")



            
def view_all():                                 #defines funtion to view all tasks available
    print("\nYou have selected to View All tasks information.\n")
    key_start = 0
    tasks_list = []                             #creates a list of tasks
    tasks_dict = {}                             #creates a dictionary of tasks
    
    task_file = open('tasks.txt', 'r', encoding='utf-8')           #opens tasks file in read mode
            
    for line in task_file:                      #loops to manipulate string in text file
        line = line.strip("\n")
        tasks_info = line.split(",")
        key_start += 1
        tasks_list = tasks_info
        (key, value) = key_start, tasks_info 
        tasks_dict[key] = tasks_info            #updates dictionary

        print("Task No:\t\t ", key_start)       #displays all information
        print("Title:\t\t\t", tasks_list[1])
        print("Assigned to:\t\t ", tasks_list[0])
        print("Date Assigned:\t\t", tasks_list[3])
        print("Due Date:\t\t", tasks_list[4])
        print("Task Complete:\t\t", tasks_list[5])
        print("Task Description:\t",tasks_list[2])
        print()
    


        
def view_mine():                                #defines function to view information for logged user only
    print("\nYou have selected to View your task information\n")
    with open('tasks.txt', 'r', encoding='utf-8') as task_file:   #opens tasks text file in read mode
        key_start = 0
        tasks_list = []                         #tasks list
        tasks_dict = {}                         #tasks dictionary
            
        for line in task_file:
            line = line.strip("\n")             #loops to manipulate string in text file
            tasks_info = line.split(",")
            key_start += 1
            tasks_list = tasks_info             #update list
            (key, value) = key_start, tasks_info 
            tasks_dict[key] = tasks_info        #update dictionary

            if logged_user == tasks_list[0]:    #display information for specific user
                print("Task No:\t\t ", key_start)
                print("Title:\t\t\t", tasks_list[1])
                print("Assigned to:\t\t ", tasks_list[0])
                print("Date Assigned:\t\t", tasks_list[3])
                print("Due Date:\t\t", tasks_list[4])
                print("Task Complete:\t\t", tasks_list[5])
                print("Task Description:\t",tasks_list[2])
                print()
    
   


def admin_options():                            #function to define options available for admin user
    print()                                     #displays info
    print("Admin Menu, please select one of the following options:")
    print("\tds  - display statistics")
    print("\tau  - create a new user in users' file")
    print("\tat  - create a new task in tasks' file")
    print("\ts   - to skip this menu and go to the next")
    print




def add_user():                                 #funtion for adding a new user
    print("\nYou have selected to Add New User.\n")
    with open('user.txt', 'a', encoding='utf-8') as user_file:             #opens user file in append mode to add:
        user_file.write("\n")                   #begins at the next available line
        credentials = False
                      
        i = 0
        team_members = int(input("\nEnter the number of users you would like to add: "))      #gets number from user

        for i in range (team_members):                      #loop gets login details for the number specified
            username = input("\nCreate a username: ")
            print("\nPlease note password should contain 5 or characters, any characters and at least one number.")
            password = input("Please enter a password: ")
                      
            #check password strenghth
            length = input("\nIs your password 5 characters long or more?: (Yes/No) ")
            characters = input("Does your password contain small case characters? (Yes/No) ")
            digit = input("Does your passowrd contain at least one digit? (Yes/No) ")

            if length == "Yes" and characters == "Yes" and digit == "Yes":            #if all conditions for strong password are met
                credentials = True

            if credentials == True:                   #if correct details then:
                assignment = f"{username}, {password}"          #format on user text file
                user_file.write(assignment)                     #writes credentials to file
                      
                print("\nYou have successfully created login credentials.")
        
            if length != "Yes" or characters != "Yes" or digit != "Yes":
                credentials == False                  #if conditions are not met
                print("\nThe password you have entered is not acceptable, user credentials will not be created")



        
def display_statistics():               #defines function to display statistics
    print("\nYou have selected to Display Statistics\n")
    tasks_count = 0                     #initializes count
            
    with open('task_overview.txt', 'r', encoding='utf-8') as f_task:         #opens user file in read mode
        for line in f_task:             #for loop to manipulate string
            line = line.strip("\n")

            if line.startswith("Total"):    #seeks information for total number of tasks from text file
                line = line.split(":")
                total = line[1]
        print(f"\nThe total count of tasks is: {total}")

    
    with open('user_overview.txt', 'r', encoding='utf-8') as f2_task:         #opens user file in read mode
        for line in f2_task:
            line = line.strip("\n")
    
            if line.startswith("Total Users"):  #seeks information for total number of users from text file
                line = line.split(":")
                total_use = line[1]
        print(f"\nThe total count of users is: {total_use}")

    with open('task_overview.txt', 'r', encoding='utf-8') as f_task:
        print("\nAll Tasks Reports: \n")        #prints all info read from file
        for line in f_task:
            
            line = line.strip("\n")
            print(line)

    with open('user_overview.txt', 'r', encoding='utf-8') as f2_task:         #opens user file in read mode
        print("\nAll Users Reports: \n")        #prints all info read from file
        for line in f2_task:
            line = line.strip("\n")
            print(line)
            


def file_edit():                            #define a function that manipulates text file to update any changes or edits the user might make
    task_edit = open('tasks.txt', 'r+')     #opens file then reads
    lines = task_edit.readlines()
    task_edit.close()
    del lines[task_selection-1]             #deletes a specific line that corresponds to task that user is editing
                    
    task_edit_write = open('tasks.txt', 'w+')   #opens again in write mode
    for line in lines:
        task_edit_write.write(line)         #write updated file with deleted lines
    task_edit_write.close()

    task_edit_new = open('tasks.txt', 'a')  #opens file as append mode
    task_edit_new.write(f"\n{select_list[0]}, {select_list[1]}, {select_list[2]}, {select_list[3]}, {select_list[4]}, {select_list[5]}")    #adds new edited task
    task_edit_new.close()





#This section of the program is for logging a user to to access the program.
#The correct username and password should be entered for successful login
            
        
login = False                                                   #intializes start condition for login

with open('user.txt', 'r', encoding='utf-8') as user_file:      #opens user file in read mode
    contents = user_file.read()                                 #reads the contents in user file
    contents = contents.replace(",", "").split()                #removes the commas in user file
    
    print("Welcome to TASK MANAGER! To access program please login: ")          #displays message
    login_username = input("\nEnter your login username: ")               #gets login username from user
    login_password = input("Enter your login password: ")               #gets password from user
    
    
    login_loop = True                   #initializes login loop
    while login_loop:                   #loops during login
        for line in contents:           #loops/iterates all lines in file
            
        #Check if username and password matches whats in file
            if line.startswith(login_username) and line.endswith(login_password):       #if first word is the entered username and last word is the password
                login = True                    #successful login
                login_loop = False              #end loop
                logged_user = login_username    #gets the user that has logged in
                print(f"\nYou have successfully logged in, welcome {logged_user}")

        if login_loop:                          #user stays in the loop if the login details do not match until correct details have been provided.
            print("\nInvalid login! Either your username is invalid or the password does not match")
            login_username = input("\nEnter your username: ")
            login_password = input("Enter your login password: ")


                  

#This section of the program is for when the admin user is logged in.
            
    if logged_user == "admin":                  #if the current user is admin:
        admin_options()                         #calls the admin_option function

        admin_menu = input("\nPlease select an option from the menu above before you can access the ordinary menu: ")       #gets option selection from admin user
        if admin_menu == "au":                  #if this 'option' admin adds new user to text file call add user function
            add_user()
        
        elif admin_menu == "at":                #if admin selects this option to write new task call function
            add_task()                
            
        elif admin_menu == "ds":                 #if option to display statctics call function
            display_statistics()
                         
        elif admin_menu == "s":                 #skip to next menu
            pass
        else:
            print("Invalid selection")




#This section of the program is for login of the rest of the users:
#There are various options to choose from
            
if login:
    menu_options()


    

#This section of the program opens tasks and users file to use to read information for all the options.
#The information is compiled to a list and to a dictionary and used accordingly

#Tasks information  
    key_start = 0                       #initializes dictionary count
    tasks_list = []                     #generates empty list
    tasks_dict = {}                     #generates empty dictionary
    
    with open('tasks.txt', 'r', encoding='utf-8') as task_file:          #opens tasks file in read mode
                
        for line in task_file:          #for loop to manipulate string in text file to read info
            line = line.strip("\n")
            tasks_info = line.split(",")
            key_start += 1
            tasks_list = tasks_info
            (key, value) = key_start, tasks_info 
            tasks_dict[key] = tasks_info        #updates dictionary

 
#Users Information
    count = 0                           #initializes dictionary count
    users_dict = {}                     #generates empty dictionary

    with open('user.txt', 'r', encoding='utf-8') as user_file:        #opens user file in read mode

        for username in user_file:
            count += 1
            contents = username.split(',')
            contents = contents[0]
        
            users_dict[count] = contents            #updates user dictionary
        users_list = users_dict.values()




#This section is now for all the various options on the menu.
#It pulls information from the user and task dictionaries above

        
    ordinary_option = input("\nSelect an option from the Ordinary menu: ")          #gets menu selected option of the main/ordinary menu
    
    if ordinary_option == "r" and logged_user == "admin":               #if option but only available for 'admin' user call function
        reg_user()
        
    elif ordinary_option == "a":                              #if option to add task call function
        add_task()

    elif ordinary_option == "vm":                           #if option to view users's task call funtion
        view_mine()

    elif ordinary_option == "va":                           #if option to view all tasks call function
        view_all()




#This section is for allowing the user to select either a specific task from all tasks by entering a number or input ‘-1’ to return to the main menu.
#It also allows the user to edit the task that they have selected

        task_selection = int(input("Select a task by entering corresponding number: "))     #gets task selection input from user
        valid_selection = False
        
        while task_selection != -1:                         #loops as long as user does not enter '-1'
            if task_selection in tasks_dict:
                select_list = tasks_dict[task_selection]
                valid_selection = True
                
                print("\nm\t- mark task as complete")       #displays options to edit tasks
                print("e\t- edit task")
                print("c\t- cancel")
                
                action = input("\nSelect an action to perform: ")   #gets action input from user
                
                if select_list[5] == " Yes":                #if task has already been completed it cannot be modified
                    print("Task has already been completed therefore cannot be edited!")
                    break
                
                if action == "m" and select_list[5] != " Yes":      #if not completed mark as complete in this section
                    select_list[5] = " Yes"
                    print(f"\nTask {task_selection} is now marked as complete")
                    tasks_dict[task_selection] = select_list
                    
                    file_edit()
                    
                    break
                
                elif action == "e" and select_list[5] != " Yes":    #edits task infomation
                    select_list = tasks_dict[task_selection]

                    further_select = input("What task information would you like to edit? (User, Due date, Both) or c to cancel: ")

                    if further_select == "User":
                        select_list[0] = input("Edit user name: ")
                        print(f"\nTask {task_selection} is now assigned to {select_list[0]}")

                    elif further_select == "Due date":
                        select_list[4] = input("\nEdit due date, format dd Month YYYY: ")
                        print(f"\nThe due date for task {task_selection} is now {select_list[4]}")

                    elif further_select == "Both":
                        select_list[0] = input("Edit user name: ")
                        select_list[4] = input("\nEdit due date, format dd Month YYYY: ")
                        print(f"\nTask {task_selection} is now assigned to {select_list[0]} and the new due date is {select_list[4]}")
                        
                    elif further_select == "c":
                        pass
                    else:
                        print("Invalid selection!")
                    
                    tasks_dict[task_selection] = select_list

                    file_edit()
                    break
                
                elif action == "c":                                 #if user does not want to edit, user can skip by 'cancelling'
                    break
                
            elif task_selection not in tasks_dict:                  #checks for validity of task selection by user, it has to be available in dictionary
                valid_selection = False
            print("Invalid task selection")
            break
            
        
#This section is for generating reports and displaying the information accordingly
        
    elif ordinary_option == "gr":
        print("\nYou have selected to Generate Reports/\n")
        
        f1 = open('task_overview.txt', 'w', encoding='utf-8')                         #create ouput text files or modify if it already exist.
        f2 = open('user_overview.txt', 'w', encoding='utf-8')
        f1.write("Tasks information:\n")
        

#For the Tasks Overview file:
        all_tasks = len(tasks_dict)                         #assigns length of dictonary to variable


        value = 0
        complete_count = 0
        incomplete_count = 0
        
        for value in tasks_dict:                            #loop to count complete and incomplete tasks
            separate_list = tasks_dict[value]               #for each task separate the info in the dictionary
            
            if separate_list[5] == " Yes":                  #count if complete
                complete_count += 1
                
            elif separate_list[5] == " No":                 #coun if incomplete
                incomplete_count += 1
                
        percent_incomplete =  round((incomplete_count/ len(tasks_dict) * 100), 2)       #performs calculations for percentages


#Display all the information, not very necessary however because admin user can pull more organized information from output files
        
        print("\nTask Overview:")
        print("(NB: Admin can access these numbers in detail)")
        print("\nTotal of all tasks: ", all_tasks)
        print("Total number of complete tasks: ", complete_count)
        print("Total number of incomplete tasks: ", incomplete_count)

        
        overdue_count = 0
        for value in tasks_dict:                            #loop for tasks that are overdue
            separate_list = tasks_dict[value]
            date_today = date.today()                       #gets current date using the datetime module 
            due_date = datetime.datetime.strptime(separate_list[4], ' %d %B %Y')    #convert due date to format of datetime module
            due_date = due_date.date()

            if due_date < date_today and separate_list[5] == " No":                 #dates are now comparable
                overdue_count += 1
                    

        percent_overdue = round((overdue_count/ len(tasks_dict) * 100), 2)          #displays more information
        print("Number of overdue tasks is: ", overdue_count)
        print("Percentage of incomplete tasks: ", percent_incomplete)
        print("Percentage of overdue tasks: ", percent_overdue)


#This section writes the information from generate reports to output file, Tasks_Overview
        
        f1.write(f"Total: {all_tasks}")
        f1.write(f"\nCompleted: {complete_count}")
        f1.write(f"\nIncomplete: {incomplete_count}")
        f1.write(f"\nOverdue: {overdue_count}")
        f1.write(f"\nPercentage Incomplete: {percent_incomplete}%")
        f1.write(f"\nPercentage Overdue: {percent_overdue}%")




#Now generae report from users information:

        total_users = len(users_dict)                       #total users is length of users dictionary
        all_tasks = len(tasks_dict)                         #total tasks is length of users dictionary
        
        print("\nTotal number of users is: ", total_users)  #Display
        print("Total number of tasks is: ", all_tasks)


        f2.write(f"Users Information:\n")                   #write information to User_Overview function 
        f2.write(f"Total Users: {total_users}\n")
        f2.write(f"Total Tasks: {all_tasks}\n")


#Initialize start values for counts:
        user_count = 0
        user_overdue = 0
        user_complete = 0
        user_complete_perc = 0
        user_overdue = 0

        print("\nUser Overview:")                           #displays
        print("(NB: Admin can access these numbers in detail)")
        
        for user in users_dict.values():                    #for each user in the dictionary and for correspnding task obtain information
            for value in tasks_dict:
                separate_list = tasks_dict[value]
                
                if separate_list[0] == user:
                    user_count += 1
                    
                    if user_count == 0:                     #if there are no tasks assigned to user at any given moment:
                        user_count = 0.00000000000000000001 #divide by a minute/negligible number to avoid dividing by 0 which is mathematically incorrect
                        
                    percent_assigned = round((user_count/len(tasks_dict)*100), 2)

                    if separate_list[5] == " Yes":
                        user_complete += 1

                    if separate_list[5] == " No":
                        date_today = date.today()
                        due_date = datetime.datetime.strptime(separate_list[4], ' %d %B %Y')
                        due_date = due_date.date()

                        if due_date < date_today:           #compares dates in input file with curent date to see if overdue
                            user_overdue += 1
            
            if user_count == 0:                             #if there are no tasks assigned to user at any given moment:
                        user_count = 0.00000000000000000001 #divide by a minute/negligible number to avoid dividing by 0 which is mathematically incorrect
            user_complete_perc = round((user_complete/user_count*100), 2)
            user_to_complete = 100 - user_complete_perc
            perc_user_overdue = round((user_overdue/ user_count * 100), 2)
            

#Display all the information, not very necessary however because admin user can pull more organized information from output files
            
            print("\n" + user + ":")
            print(f"Number of tasks assigned to {user} are: {user_count}")
            print(f"Percentage of tasks assigned to {user} is: {percent_assigned}")
            print(f"Completed tasks by {user} are: {user_complete}")
            print(f"Percentage of completed tasks by {user} is: {user_complete_perc}")
            print(f"Percent of tasks to be completed by {user} is: {user_to_complete}")
            print(f"Number of {user}'s overdue tasks is: ", user_overdue)
            print(f"Percentage of {user}'s overdue tasks is: ", perc_user_overdue)

    
#This section writes the information from generate reports to output file, User_Overview
            
            f2.write(f"\nUser: {user}\n")
            f2.write(f"Tasks Assigned: {user_count}\n")
            f2.write(f"Percentage Assigned: {percent_assigned}\n")
            f2.write(f"Percentage Completed: {user_complete_perc}%\n")     
            f2.write(f"Percentage Incompleted: {user_to_complete}%\n")
            f2.write(f"Percentage Overdue: {perc_user_overdue}%\n")


#Reset all the counts and the same variable for each user's count
            
            user_count = 0              #reset count
            percent_assigned = 0
            user_overdue = 0
            user_complete = 0
            user_complete_perc = 0
            user_overdue = 0
            perc_user_overdue = 0

        f1.close()                      #closes file
        f2.close()
        
        
    elif ordinary_option == "ds":       #if option, perform a check for logged user, option only available to admin
        if logged_user == "admin":
            pass
        else:
            print("Option only available to admin user! Login as admin to view Statistics")
            

    elif ordinary_option == "e":                           #if option to exit the program, confirm exit
            exit(0)                                            #terminates program

           
    elif ordinary_option == "r" and logged_user != "admin":     #displays error message if a user other user tries to access
        print("Option only available to admin user! Login as admin to register user")
        
    
    elif ordinary_option != "r" or ordinary_option != "a" or ordinary_option != "vm" or ordinary_option != "va" or ordinary_option != "e":      #if none of the menu selections are selected
        print("\nInvalid selection!")

    



