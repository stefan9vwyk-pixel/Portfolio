# ==========Inventory Management System==========
# Import necessary modules for use in program.
from tabulate import tabulate
# Create Shoe class
class Shoe:
    """Class representing a shoe object"""

    def __init__(self, country, code, product, cost, quantity):
        '''
        Initializes a shoe object with specified country, code,
        product, cost and quantity
        '''

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Define a method to get the cost of a shoe and return it
    def get_cost(self):
        '''
        Method to get the cost of a shoe
        '''
        return f"The cost of the selected shoe is : {self.cost}"

    # Define a method to get the stock quantity of a shoe and return it
    def get_quantity(self):
        '''
        Method to get the quantity of a shoe
        '''
        return f"The stock quantity of the selcted shoe in is : {self.quantity}"

    # Define a method to represent each object as string
    def __str__(self):
        '''
        Method to represent object as string
        '''
        return (f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}")


#==========Functions outside the class==============
def read_shoes_data():
    '''
    Function to read from the 'inventory.txt' file and capture each line as 
    a shoe object and append it to the shoe_list variable

    Return:
        Each object capured in shoe_list
    '''
    # Code to prevent File not found error, and inform user file was not found.
    try:
        with open("inventory.txt", 'r', encoding='utf-8') as file: # Open text file and read from it.
            for line in file: # Iterate through each line in the file.
                if line.startswith("Country"): # Skip the header line
                    continue

                # Strip each line and split into sublist
                data = line.strip()
                data = data.split(",")

                # Create Shoe object using data from file and append to shoe_list 
                shoe_list.append(Shoe(data[0], data[1], data[2], float(data[3]), int(data[4])))

    except FileNotFoundError: # Handle error if file does not found.
        print("File was not found, please check file directory.")


def capture_shoes():
    '''
    Function to take user input and create new Shoe object and append the object to 'shoe_list' variable.
    '''
    # Get necessary user inputs to create new shoe object
    country = input("Enter the manufacturing country : ").title() # Ask user to input country   
    code = input("Enter the product code : ").upper() # Ask user to input the product code    
    product = input("Enter the product name : ").title() # Ask user to input the product name

    while True: # Loop to prevent an error
        try: # Try to get correct user input 
            cost = float(input("Enter the cost of the product : ")) # Ask user to input the cost of the product
            break
        except ValueError: # Handle exception if input is wrong
            print("Invalid input, only type the number.")

    # Use same exception handling as above to prevent incorrect user input
    while True: 
        try:
            quantity = int(input("Enter the quantity of the product in stock : ")) # Ask user to input the quantity of the product
            break
        except ValueError:
            print("Invalid input, only type the number.")

    # Create new Shoe object using user inputs and append to the shoe_list
    shoe_list.append(Shoe(country, code, product, cost, quantity))

    print(" ") # Added empty line for easier readibility
    print("The new product with the folloing details will be captured into the system.\n" \
          f"{country}, {code}, {product}, {cost}, {quantity}")


def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes in table format.
    '''
    # I used list comprehention to capture the needed info into a new list.
    table_data = [[shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity] for shoe in shoe_list]
    table_headers = ["Country", "Code", "Product", "Cost", "Quantity"] # Table headers for the tabulate function

    # Used tabulate function to print the list of shoes
    print(tabulate(table_data, headers=table_headers, tablefmt="fancy_grid"))


def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    '''
    # Find the lowest quantity and print out message to user
    lowest_quantity = min(shoe_list, key=lambda shoe: shoe.quantity) 
    print(f"The product with the lowest quantity is {lowest_quantity.product}, {lowest_quantity.code} with {lowest_quantity.quantity} in stock.\n")

    # Using exception handling to handle incorrect input form user
    while True:
        # Ask the user if they want to add to the current quantity
        user_choice = input("Would you like to add to this quantity?\n" \
        "1.\tYes\n" \
        "2.\tNo\n" \
        "Type option here : ")
        
        # If-else to determin next step based on user input
        if user_choice == "1": # If user chose first option, run function to add to quantity
            while True: # Used loop to handle exception for incorrect input
                try:
                    add_quantity = int(input("\nEnter the amount of stock you would like to add to current stock : ")) # Ask user hoe much they would like to add
                    break
                except ValueError: # Hanle esception if input is incorrect
                    print("Incorect input. Only input the number and try again")

            for shoe in shoe_list: # Use for-loop to iterate over the shoe_list and find the correct shoe to update
                if shoe.quantity == lowest_quantity.quantity: # Check for correct shoe object
                    shoe.quantity += add_quantity # Add the user's specified quantity to the shoe object's current quantity
                    break # To stop iterating over list if correct shoe was found
            print(f"The stock for {lowest_quantity.product} will be updated.") # Print confirmation message to user
            break # To break out of first while loop
        elif user_choice == "2": # User chose second option, do nothing 
            return
        else: # If user typed wrong, print message and restart the loop
            print("\nYour input was incorrect, please try again.\n")


def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    # Ask user to type the code of the shoe they are looking for, regardless of case sensitivity
    shoe_code = input("Please enter the code of the product you want to search for : ").upper()
    # Iterate over shoe_list to find the correct shoe
    for shoe in shoe_list:
        if shoe_code == shoe.code: # Check if the shoe code matches the user input
            print(shoe) # Print object
            break # To stop iterating over the list if correct shoe was found
    else: # If user input was wrong or the code is not found, print message to user
        print("Product with the above mentioned code does not exist, please check if code is correct and try again.")


def value_per_item():
    '''
    Function to take the cost and quantity of each object in shoe_list,
    multiply the 2 items and print the value.
    '''
    # List comprehention to create new list with necessary data for function
    table_data = [[shoe.product, int(shoe.cost), shoe.quantity] for shoe in shoe_list]
    # Used a for-loop to iterate over each item in list and calculate the value
    for lines in range(len(table_data)):
        value = table_data[lines][1] * table_data[lines][2] # Calculate the value for each sublist in the table_data list
        table_data[lines].append(value) # Append the value back to each corresponding sublist
    
    table_headers = ["Product", "Cost", "Quantity", "Value"] # Create table headers 

    # Create a table to print to user for easy readability, using the table_data and tanble_headers lists
    print(tabulate(table_data, headers=table_headers, tablefmt="fancy_grid")) 


def highest_qty():
    '''
    Function to find the product with the max quantity.
    '''
    # Find the highest quantity using the max() function
    highest_quantity = max(shoe_list, key=lambda shoe: shoe.quantity)
    # Print highest quantity to user 
    print(f"{highest_quantity.product} has the highest quantity with {highest_quantity.quantity} in stock" \
          " and is on sale at the moment.")
     

#==========Main Menu=============

# Create a list to store the shoe objects
shoe_list = []

read_shoes_data() # Execute the function to populate shoe_list with objects

print("Welcome to the inventory management system.") # Print welcome message
print("-" * 43 + "\n")
while True: # Loop until user decides to end progrem
    # Print menu with option for user
    print("Please choose from the list of options below:")
    print("1.\tView currect products\n" \
          "2.\tSearch for specific product\n" \
          "3.\tView the value for all products\n" \
          "4.\tCapture new product\n" \
          "5.\tView product with lowest quantity\n" \
          "6.\tView product with highest quantity\n" \
          "7.\tTo end the program")
    user_choice = input("Type option here : ") # Ask user to input their option
    print(" ") # Added empty lines to serve as new lines for readibility
    # Run correct function depending on user input
    if user_choice == "1":
        view_all()
        print(" ")
    elif user_choice == "2":
        search_shoe()
        print(" ")
    elif user_choice == "3":
        value_per_item()
        print(" ")
    elif user_choice ==  "4":
        capture_shoes()
        print(" ")
    elif user_choice == "5":
        re_stock()
        print(" ")
    elif user_choice == "6":
        highest_qty()
        print(" ")
    elif user_choice == "7":
        print("Thank you for using the program. Untill next time, Goodbye.")
        break
    else:
        print("Your input was incorrect, please try again. Only type the number, else make sure the number typed is correct.\n") # Print message if user input was incorrect.

# ======== End of code =========