# ===== Importing external modules ===========
from pathlib import Path
from datetime import datetime

# Got following code with help of Google, I was having trouble finding
# The user.txt file so I implemented the code to help with that

# Find the path of the current python script file
script_dir = Path(__file__).parent
# Use the script path to locate the text files needed for the program
user_path = script_dir / "user.txt"
task_path = script_dir / "tasks.txt"
task_over = script_dir / "task_overview.txt"
user_over = script_dir / "user_overview.txt"

# Using the above code made opening the text files a lot easier,
# All I need to do is use the variable name instead of the file name
# And i can keep all the text files in the same directory as the python script


def reg_user():
    """
    This function allows the admin user to register a new user by entering a
    unique username and a password. The function checks if the username
    already exists and returns to the main menu if it does.
    """
    # Check if username already exists
    while True:
        new_username = input("Please enter the Username of the new User : ")

        if new_username in users:
            print("A user with that username already exists, "
                  "please try again.")
            return  # Return to main menu if username already exists
        else:
            break

    # Check if password and confirm password match
    while True:
        new_password = input("Please enter a Password for the new User : ")
        confirm_password = input("Please confirm Password : ")

        if new_password == confirm_password:
            print("New User will be added.")
            break  # Break out of loop if passwords match
        else:
            print("Passwords do not match, please try again.")

    # Write credentials to users.txt file
    with open(user_path, "a+", encoding="utf-8")as file:
        file.write("\n" + new_username + ", " + new_password)

    while True:
        try:
            # Open file to read lines from file
            with open(user_path, "r", encoding="utf-8") as file:
                for lines in file:
                    user = lines.strip().split(", ")
                    if len(user) != 2:
                        continue
                    key, value = user  # Save each line as key and value
                    users[key] = value  # Separate the key and value
            break
    # Exception for File not found error
        except FileNotFoundError:
            print("File was not found, please check directory.")


def add_task():
    """
    This function allows the user to add a new task,
    and saves the task details to the tasks.txt file.
    The function also checks if the username to
    Whom the task is assigned exists in the system,
    and returns to the main menu if it does not.
    """
    # Check if user exists to assign task to
    while True:
        new_task_user = input(
            "Enter the username to whom the task should be assigned : "
        )
        if new_task_user not in users:
            print("User does not exist, please try again.")
            return  # Return to main menu if user does not exist
        else:
            break  # Break out of loop if user exists

    # Get the rest of the task details from user input
    new_task_title = input("Enter the title of the new task : ")
    new_task_desc = input(
            "Enter a short description of the task : "
        )
    new_task_due = input(
            "When should this task be completed? i.e., 01 Jan 2000 : "
        )
    new_task_assign = input("Enter today's date i.e., 01 Jan 2000 : ")

    # Write the new task details to tasks.txt file
    with open(task_path, "a", encoding="utf-8") as file:
        file.write(
            f"\n{new_task_user}, {new_task_title}, "
            f"{new_task_desc}, {new_task_assign}, "
            f"{new_task_due}, No"
        )


def view_all():
    """
    This creates a list of all the tasks in the tasks.txt file
    and prints them in a readable format.
    """
    tasks = []  # Empty list to save tasks from tasks.txt file
    # Try to open the tasks.txt file and read from it
    try:
        with open(task_path, "r", encoding="utf-8") as file:
            for line in file:
                task = line.strip().split(", ")
                # Check if the line is not empty and has at least 6 elements
                if task and len(task) >= 6:
                    tasks.append(task)

    except FileNotFoundError:  # Exception for File not found error
        print("File was not found, please check directory.")

    print("-" * 50)  # Added code to make output neat and easy to read

    # Print each task in a readable format, using the index to number the tasks
    for index, task in enumerate(tasks, start=1):
        print(f"{index}\tTask : \t\t\t {task[1]}\n"
              f"\tAssigned to : \t\t {task[0]}\n"
              f"\tDate assigned : \t {task[3]}\n"
              f"\tDue date : \t\t {task[4]}\n"
              f"\tTask Complete? \t\t {task[5]}\n"
              f"\tDescription : \n\t {task[2]}")
        print("-" * 50)  # Spilt the tasks with a line for better readability


def view_mine():
    """
    This function creates a list of tasks assigned to the
    currently logged in user and prints them in a readable format.
    """
    def edit_task(index):
        """
        This function allows the user to edit a task that is assigned to them.
        User can only edit a task that is not marked as completed.
        If user wishes to edit task, they can choose to reassign the task to
        another user or change the due date of the task.

        Args :
        index (int) : The index of the task to be edited
        """
        # Select the task to be edited using the index provided by the user
        edit_task = my_tasks[index - 1]

        # Ask the user if they want to edit the task or mark it as completed
        user_choice = input("Please select an option :\n"
                            "edit - Edit selected task\n"
                            "done - Mark task as completed?\n"
                            ": ").lower()

        # If user selects done, mark the task as completed
        # By changing the value the 6th element of the task to "Yes"
        if user_choice == "done":
            edit_task[5] = "Yes"

        # If user selects edit, check if the task is not completed
        elif user_choice == "edit":
            if edit_task[5] == "No":
                # Ask user what they want to assign task to someone else
                while True:  # Loop to handle any incorrect input from user
                    reassign_user_option = input(
                        "Would you like to assign the selected task to "
                        "someone else? (yes/no) : "
                    ).lower()
                    if reassign_user_option == "yes":
                        reassign_user = input(
                            "Please enter the username of the user to "
                            "whom the task must be assigned to : "
                        )
                        # Check if the user exists before reassigning the task
                        if reassign_user in users:
                            edit_task[0] = reassign_user
                            print(f"Task was assigned to {reassign_user}.")
                            break
                        else:  # Print message if user does not exist
                            print("User with that username does not exist, "
                                  "please try again.")

                    elif reassign_user_option == "no":
                        # Break out of loop if user does not want,
                        # To reassign task
                        break
                    else:
                        print("Incorrect input, try again.")

                # Loop to handle any incorrect input from user
                while True:
                    # Ask user if they want to change the due date of the task
                    due_option = input(
                        "Would you like to change the date the task must "
                        "be completed? (yes/no) : "
                    ).lower()

                    if due_option == "yes":
                        # Ask user to input the new due date
                        change_due_date = input(
                            "Please enter the new date the task must be "
                            "completed i.e., 01 Jan 2000 : "
                        )
                        # Update the task with the new date
                        edit_task[4] = change_due_date
                        print(
                            f"The due date of the task was changed to "
                            f"{change_due_date}."
                        )
                        break  # Break out of loop
                    elif due_option == "no":
                        # Break out of loop if user does not want
                        # To change due date
                        break

                    else:
                        print("Incorrect input, try again.")

            # If the task is marked as completed,
            # Print message and return to main menu
            elif edit_task[5] == "Yes":
                print(
                    "This task has been completed and thus cannot be "
                    "edited."
                )
        else:
            print("Incorrect input, returning to main menu.")
            # Return to main menu if user input is incorrect instead of looping
            # I decided to return to main menu if user input is incorrect to
            # Avoid too many loops that could potentially cause infinite loops
            return
        lines = []
        # Update the tasks.txt file with the edited task details
        # Read the tasks from the file and save them in a list
        with open(task_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip().split(", ")
                # Skip any empty lines or
                # Lines that do not have at least 6 elements
                if line and len(line) >= 6:
                    lines.append(line)

        # Rewrite any non edited tasks to the file and
        # Update the edited task with the new details
        with open(task_path, "w", encoding="utf-8") as f:
            for line in lines:
                # Check for task to be edited using the title of the task,
                # and update the task with the new details
                if line[1] == edit_task[1]:
                    f.write(
                        f"{edit_task[0]}, {edit_task[1]}, "
                        f"{edit_task[2]}, {edit_task[3]}, "
                        f"{edit_task[4]}, {edit_task[5]}\n"
                    )
                else:  # Write the non edited tasks as is
                    f.write(", ".join(line) + "\n")

        return

    def get_valid_task_number():
        """
        Recursive function to ensure the user picks a valid task index
        or exits with -1.

        Returns:
        int: The valid task number entered by the user
        """
        # Ask user for the index number of the task they wish to edit
        task_selected = (input(
                "Enter the number of the task you wish to edit "
                "or -1  to return to main menu : "
            ))
        # Base case: If user wants to return to main menu, return -1
        if task_selected == "-1":
            return -1

        # check if input in an integer
        if task_selected.isdigit():
            index = int(task_selected)

            # Check if input is a valid index number for the tasks list
            if 1 <= index <= len(my_tasks):
                return index

            # Recursive call if index is out of range
            else:
                print(f"invalid index, please enter a number "
                      f"between 1 and {len(my_tasks)}.")
                return get_valid_task_number()

        # Recursive call if input is not an integer
        else:
            print("Invalid input, enter a number")
            return get_valid_task_number()

    # Attempt to open the tasks.txt file and read from it
    try:
        with open(task_path, "r", encoding="utf-8") as file:
            for line in file:
                if line.startswith(username):
                    my_task = line.strip().split(", ")
                    # Check if the line is not empty
                    # And has at least 6 elements
                    if my_task and len(my_task) >= 6:
                        my_tasks.append(my_task)
                else:
                    continue

    # Exception for File not found error
    except FileNotFoundError:
        print("File was not found, please check directory.")

    # Print each task assigned to the user in a readable format,
    # using the index to number the tasks
    print("-" * 50)
    if my_tasks:
        for index, task in enumerate(my_tasks, start=1):
            print(f"{index}\tTask : \t\t\t {task[1]}\n"
                  f"\tAssigned to : \t\t {task[0]}\n"
                  f"\tDate assigned : \t {task[3]}\n"
                  f"\tDue date : \t\t {task[4]}\n"
                  f"\tTask Complete? \t\t {task[5]}\n"
                  f"\tDescription : \n\t {task[2]}")
            print("-" * 50)
    else:  # Print message if user has no tasks assigned
        print("You have no tasks assigned.")
        print("-" * 50)

    task_selected = get_valid_task_number()

    if task_selected != -1:
        edit_task(task_selected)
    else:
        return


def view_completed():
    """
    This function reads the tasks from the tasks.txt file,
    filters out the completed tasks,
    and prints them in a readable format.
    """
    # Attempt to open the tasks.txt file and read from it
    try:
        any_completed = False  # Flag to check if any completed tasks are found
        with open(task_path, "r", encoding="utf-8") as file:
            for line in file:
                task = line.strip().split(", ")
                # Check if the line is not empty and has at least 6 elements
                if task and len(task) >= 6:
                    # Check if the task is marked as completed and print
                    # it in a readable format
                    if task[5] == "Yes":
                        # Set flag to True if a completed task is found
                        any_completed = True
                        print(f"Task : \t\t\t {task[1]}\n"
                              f"Assigned to : \t\t {task[0]}\n"
                              f"Date assigned : \t {task[3]}\n"
                              f"Due date : \t\t {task[4]}\n"
                              f"Task Complete? \t\t {task[5]}\n"
                              f"Description : \n\t {task[2]}")
                        print("-" * 50)

        # Print message if no completed tasks are found
        if not any_completed:
            print("None of the tasks are completed.")

    except FileNotFoundError:  # Exception for File not found error
        print("File was not found, please check directory.")


def delete_task():
    """
    This function allows the user to delete a task from the tasks.txt file.
    The view_all() function is called to display all the tasks
    with their index numbers and the user is prompted to
    enter the index number of the task they wish to delete.
    """
    view_all()
    # Loop to handle any incorrect input from user
    while True:
        try:
            # Ask user for the index number of the task they wish to delete
            task_selected = int(input(
                "Enter the number of the task you wish to delete "
                "or -1  to return to main menu : "
            ))
            break
        except ValueError:
            # Exception for Value error if user input is not an integer
            print("Only enter the index number of the task.")

    # If user input is not -1, proceed to delete the task with the
    # given index number
    if task_selected != -1:
        tasks = []

        # Read the tasks from the file and save them in a list,
        # skipping any empty lines
        with open(task_path, "r", encoding="utf-8") as file:
            for line in file:
                task = line.strip().split(", ")
                if task and len(task) >= 6:
                    tasks.append(task)

        # Check if the index number provided by the user is valid
        if task_selected <= len(tasks):
            # Delete the task with the given index number
            # from the list of tasks
            del tasks[task_selected - 1]

            # Rewrite the tasks list to the file
            with open(task_path, "w", encoding="utf-8") as file:
                for task in tasks:
                    file.write(
                        f"{task[0]}, {task[1]}, {task[2]}, "
                        f"{task[3]}, {task[4]}, {task[5]}\n"
                    )

            # Confirmation message that task was deleted
            print("Task was deleted.")

        # Print an error message,
        # If the index number provided by the user is not valid
        else:
            print("Incorrect index provided, try again.")


def generate_reports():
    """
    This function generates two reports: task overview and user overview
    Using a function defined for each report
    """
    def task_overview():
        """
        This function reads the tasks from the tasks.txt file
        Creates a list of tasks and calculates statistics such as,
        Total number of tasks, number of completed tasks,
        Number of incomplete tasks, number of overdue tasks.
        And writes these statistics to a task overview file.
        """
        tasks = []

        def count_tasks():
            """
            This function reads the tasks from the tasks.txt file,
            saves them to the tasks list and while
            keeping count of the total tasks.

            Returns: Total number of tasks in the tasks.txt file
            """
            with open(task_path, "r", encoding="utf-8") as file:
                total_tasks = 0
                for line in file:
                    task = line.strip().split(", ")
                    # Skip any empty lines or
                    # lines that do not have at least 6 elements
                    if not task or len(task) < 6:
                        continue
                    total_tasks += 1
                    tasks.append(task)
            return total_tasks

        def complete_tasks():
            """
            This function iterates through the tasks list and counts
            the number of completed tasks by checking if the
            6th element of each task is "Yes".

            Returns: Number of completed tasks in the tasks list
            """
            completed_tasks = 0
            for task in tasks:
                if task[5] == "Yes":
                    completed_tasks += 1
            return completed_tasks

        def incomplete_tasks():
            """
            This function iterates through the tasks list and counts
            the number of uncompleted tasks by checking if the
            6th element of each task is "No".

            Returns: Number of uncompleted tasks in the tasks list
            """
            uncompleted_tasks = 0
            for task in tasks:
                if task[5] == "No":
                    uncompleted_tasks += 1
            return uncompleted_tasks

        def overdue_tasks():
            """
            This checks for overdue tasks
            By iterating through the tasks list and
            Checking if the task is incomplete
            And if the due date has passed

            Returns: Number of overdue tasks in the tasks list
            """
            # Get the current date to compare with the due date of the tasks
            today = datetime.now()
            overdue_tasks = 0
            for task in tasks:
                # Check if the task is incomplete
                if task[5] == "No":
                    try:
                        # Get the due date of the task and
                        # Convert it to a datetime object
                        task_date = datetime.strptime(
                            task[4], "%d %b %Y"
                        )
                        # Compare the 2 dates
                        if task_date.date() < today.date():
                            # Increment the overdue tasks count
                            overdue_tasks += 1
                    # Exception for Value error if the date format
                    # Of the task is incorrect
                    except ValueError:
                        print("One of the task has an incorrect date "
                              "format, please correct mistake and try "
                              "again.")

            return overdue_tasks

        def percentage_incomplete(t, i):
            """
            This function calculates the percentage of tasks that are
            incomplete by dividing the number of incomplete tasks by the
            total number of tasks. Also handles the ZeroDivisionError by
            checking if the total number of tasks is greater than 0
            before performing the division

            Args :
            t: Total number of tasks
            i: Number of incomplete tasks

            Returns :
            Percentage of tasks that are incomplete
            """
            if t > 0 and i > 0:
                percentage = (i / t) * 100
                return round(percentage, 2)
            else:
                return 0

        def percentage_overdue(t, o):
            """
            This function calculates the percentage of tasks that are
            overdue by dividing the number of overdue tasks by the
            total number of tasks. Also handles the ZeroDivisionError by
            checking if the total number of tasks is greater than 0
            before performing the division

            Args :
            t: Total number of tasks
            o: Number of overdue tasks

            Returns :
            Percentage of tasks that are overdue
            """
            if t > 0 and o > 0:
                percentage = (o / t) * 100
                return round(percentage, 2)
            else:
                return 0

        # Call the above functions to get the required statistics
        total_tasks = count_tasks()
        completed = complete_tasks()
        uncompleted = incomplete_tasks()
        overdue = overdue_tasks()
        incomp_percentage = percentage_incomplete(total_tasks, uncompleted)
        overdue_percentage = percentage_overdue(total_tasks, overdue)

        # Write the statistics to the task overview file
        with open(task_over, "w", encoding="utf-8")as f:
            f.write(f"{total_tasks}, {completed}, {uncompleted}, {overdue}, "
                    f"{incomp_percentage}, {overdue_percentage}")

    def user_overview():
        # I asked google for some help with this function as I was
        # having trouble with the logic. I got the general idea of how
        # to do this but I was having trouble with the implementation.
        """
        This function reads the tasks from the task file and calculates
        Statistics for each user based on the tasks assigned to them.
        It then writes these statistics to a user overview file.
        The statistics include the total number of tasks assigned to each user,
        The percentage of tasks assigned to each user,
        The percentage of tasks completed by each user,
        The percentage of tasks incomplete for each user,
        And the percentage of overdue tasks for each user.
        """

        tasks = []

        # Read tasks.txt and fill the 'tasks' list
        try:
            with open(task_path, "r", encoding="utf-8") as file:
                for line in file:
                    task = line.strip().split(", ")
                    if task and len(task) >= 6:
                        tasks.append(task)
        except FileNotFoundError:
            print("File was not found, please check directory.")
            return  # Stop if file is missing

        total_tasks = len(tasks)
        user_stats = []

        # Get unique users who actually have tasks
        users_with_tasks = set(task[0] for task in tasks)
        user_count = len(users_with_tasks)

        # Loop through each user to calculate their specific stats
        for user in users:  # Using 'users' dict for the loop
            user_tasks_count = 0
            tasks_comp = 0
            tasks_incomp = 0
            overdue_tasks = 0
            today = datetime.now().date()

            for task in tasks:
                # Check if the task is assigned to the current user
                if task[0] == user:
                    user_tasks_count += 1

                    # Check status of the task
                    if task[5] == "Yes":
                        tasks_comp += 1
                    else:
                        tasks_incomp += 1
                        # Check if overdue (only if incomplete)
                        try:
                            task_date = datetime.strptime(
                                task[4], "%d %b %Y"
                            ).date()
                            if task_date < today:
                                overdue_tasks += 1
                        except ValueError:
                            print("Incorrect format used for task "
                                  "date, check date.")
                            pass  # Handle bad dates

            # 4. Prevent DivisionByZero if a user has 0 tasks
            if user_tasks_count > 0:
                user_task_p = (user_tasks_count / total_tasks) * 100
                p_comp = (tasks_comp / user_tasks_count) * 100
                p_incomp = (tasks_incomp / user_tasks_count) * 100
                p_overdue = (overdue_tasks / user_tasks_count) * 100
            else:
                user_task_p = p_comp = p_incomp = p_overdue = 0

            # Add this user's data to our master list
            user_stats.append([
                user, user_tasks_count, round(user_task_p, 2),
                round(p_comp, 2), round(p_incomp, 2), round(p_overdue, 2)
            ])

        # 5. Write to file
        with open(user_over, "w", encoding="utf-8") as f:
            f.write(f"{user_count}, {total_tasks}\n")
            for stat in user_stats:
                # Using f-string formatting to round percentages to 2 decimals
                f.write(f"{stat[0]}, {stat[1]}, {stat[2]}, "
                        f"{stat[3]}, {stat[4]}, {stat[5]}\n")

    # Call the above functions to generate the reports
    task_overview()
    user_overview()

    # Confirmation message that reports were generated successfully
    print("Reports were generated successfully.")


def display_stats():
    """
    This function makes use of 2 nested functions
    to read the statistics from the task overview and user overview files
    and prints the statistics in a readable format.
    """

    def display_tasks_stats():
        """
        This function reads the statistics from the task overview file
        and prints the statistics in a readable format.
        """
        # Attempt to open the task overview file and
        # Read the statistics from it
        try:
            with open(task_over, "r", encoding="utf-8") as f:
                for line in f:
                    tasks_stats = line.strip().split(", ")
                    # Print the statistics in a readable format
                    print(f"""
{"-"*50}
TASK STATISTICS
{"-"*50}
{"Total tasks :":<35} {tasks_stats[0]}
{"Tasks completed :":<35} {tasks_stats[1]}
{"Tasks incomplete :":<35} {tasks_stats[2]}
{"Tasks overdue :":<35} {tasks_stats[3]}
{"Percentage of tasks incomplete :":<35} {tasks_stats[4]}%
{"Percentage of tasks overdue :":<35} {tasks_stats[5]}%
""")

        except FileNotFoundError:
            print("Task overview file not found.")
            return  # Return early if file is not found

    def display_user_stats():
        """
        This function reads the statistics from the user overview file
        And prints the statistics in a readable format.
        """
        user_overview = []
        # Attempt to open the user overview file
        # And read the statistics from it
        try:
            with open(user_over, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip().split(", ")
                    user_overview.append(line)

        except FileNotFoundError:
            print("User overview file not found.")
            return  # Return early if file is not found

        # The first line of the user overview file contains the
        # general statistics. The rest of the lines contain the
        # statistics for each user
        # Split the general statistics and user statistics
        general_stats = user_overview[0]
        user_stats = user_overview[1:]

        # Print the general statistics in a readable format
        print("-" * 50)
        print(f"""
Total users with tasks assigned : {general_stats[0]}
Total tasks : {general_stats[1]}""")
        print("-" * 50)
        # Iterate through the user statistics
        # And print each user's statistics
        for stat in user_stats:
            print(f"""
{"-"*50}
Statistics for user : {stat[0]}
{"-"*50}
{"Total tasks :":<45}{stat[1]}
{"Percentage of tasks assigned to user :":<45}{stat[2]}%
{"Percentage of user's tasks completed :":<45}{stat[3]}%
{"Percentage of user's tasks incomplete :":<45}{stat[4]}%
{"Percentage of user's tasks overdue :":<45}{stat[5]}%""")

    # Call the above functions to display the statistics
    display_tasks_stats()
    display_user_stats()

    return


# ==== Login Section ====

users = {}  # Empty list to save user names and password from user.txt

while True:
    try:
        # Open file to read lines from file
        with open(user_path, "r", encoding="utf-8") as file:
            for lines in file:
                user = lines.strip().split(", ")
                if len(user) != 2:
                    continue
                key, value = user  # Save each line as key and value
                users[key] = value  # Separate the key and value
        break
# Exception for File not found error
    except FileNotFoundError:
        print("File was not found, please check directory.")

# Ask user to input username and password
# While loop to check if user input is correct
while True:
    username = input("Please enter your username : ")
    if username in users:  # Check if username matches keys
        password = input("Please enter your password : ")
        # If password is incorrect print relative message
        if password != users[username]:
            print("Password is incorrect, please try again")
        # If password is correct, break out of loop
        else:
            break
    else:  # Print message if username is not found
        print("Username not found, please try again.")

print("\n")

while True:
    # Check which user is using the program
    # And display the menu options accordingly,
    # Admin has more options than other users
    if username == "admin":
        menu = input("""Select one of the following options:
\u2022 \tr - register a user
\u2022 \ta - add task
\u2022 \tva - view all tasks
\u2022 \tvm - view my tasks
\u2022 \tvc - view completed tasks
\u2022 \tdel - delete tasks
\u2022 \tgr - generate reports
\u2022 \tds - display statistics
\u2022 \te - exit
: """).lower()  # Convert user input to lowercase

    # Menu for users who are not admin
    else:
        menu = input("""Select one of the following options:
\u2022 \ta - add task
\u2022 \tva - view all tasks
\u2022 \tvm - view my tasks
\u2022 \te - exit
: """).lower()

    print("\n")

    # Check the user input and call the corresponding function,

    if menu == 'r':
        reg_user()
        print("\n")

    elif menu == 'a':
        add_task()
        print("\n")

    elif menu == 'va':
        view_all()
        print("\n")

    elif menu == 'vm':
        my_tasks = []
        view_mine()
        print("\n")

    elif menu == 'vc':
        print("-" * 50)
        view_completed()
        print("\n")

    elif menu == 'del':
        delete_task()
        print("\n")

    elif menu == 'gr':
        generate_reports()
        print("\n")

    elif menu == 'ds':
        generate_reports()
        display_stats()
        print("\n")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")
