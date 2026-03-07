# Import function for program.
import sqlite3
from pathlib import Path

# ------- Function Section --------


def add_book():
    """
    This function adds a new book to the database,
    it asks the user for all the details of the book and the author,
    then it checks if the inputs are correct.

    Returns: A confirmation message if the book was added successfully.
    """

    # Ask user for details of the book and author
    # Strip the inputs to remove any leading or trailing whitespace
    id = input("Enter the Book ID of the new book : ").strip()
    title = input("Enter the Title of the book : ").strip().title()
    authorID = input("Enter the ID of the Author : ").strip()
    qty = input("Enter the quantity of the book : ").strip()
    author_name = input("Enter the Author's fullname : ").strip().title()
    country = input("Enter the Author's Country of origin : ").strip().title()

    # Check if the inputs are correct,
    # If they are then add the book to the database
    if (
        len(id) == 4
        and id.isdigit()
        and len(authorID) == 4
        and authorID.isdigit()
        and qty.isdigit()
    ):
        # Insert new book into the database
        # Use a try-except block to catch any sqlite3.IntegrityError,
        # Exceptions that occur if the book ID already exists in the database
        try:
            cursor.execute('''
                           INSERT INTO book(
                           id, title, authorID, qty)
                           VALUES (?, ?, ?, ?)
                           ''', (id, title, authorID, qty))

        # Print error message and return to main menu
        except sqlite3.IntegrityError:
            print("The Book ID already exists in the database, "
                  "please try again with a different ID.")
            return

        # Insert new author into the database
        cursor.execute('''
                       INSERT OR IGNORE INTO author(
                       id, name, country)
                       VALUES (?, ?, ?)''',
                       (authorID, author_name, country))

        db.commit()

        # Print confirmation message
        print(f"""
The following new book was captured :
Book ID :       {id}
Title :         {title}
Author ID :     {authorID}
Quantity :      {qty}
Author's name : {author_name}
Country :       {country}""")

    # If the inputs are not correct,
    # Print an error message and return to the main menu
    else:
        print("One of your inputs was incorrect, please try again.")


def update_book(id):
    """
    This function updates the quantity of a book in the database,
    using the book ID, then gives the user the option to update,
    more details of the book:
        The author details (author ID, name and country)
        The title of the book

    Args: id (str): The ID of the book to be updated

    Returns: A confirmation message if the book was updated successfully.
    """
    # Ask user for the new quantity of the book,
    # Catch any ValueError exceptions that may occur
    try:
        quantity = int(input("Please enter the new quantity of the book: "))

    except ValueError:
        print("Incorrect input, only enter a number")
        return

    # Update the quantity of the book in the database
    cursor.execute('''
                   UPDATE book
                   SET qty = ?
                   WHERE id = ?
                   ''', (quantity, id))

    db.commit()

    # Fetch the updated details of the book to show the user
    cursor.execute('''
                   SELECT title, qty
                   FROM book
                   WHERE id = ?
                   ''', (id,))

    updated_book = cursor.fetchone()

    # Check if the book was found in the database and print the updated details
    if updated_book is not None:
        print("\nThe quantity of the following book was updated : \n"
              f"Title :\t\t{updated_book[0]}\n"
              f"Quantity :\t{updated_book[1]}\n")

    # Error message if the book was not found in the database
    else:
        print("\nBook not found in the database.")
        return

    # Ask the user if they want to update more details of the book
    while True:
        should_update = input(
            "Would you like to update the Author or Title "
            "of the book?\n"
            "A:\tAuthor details\n"
            "T:\tTitle of the book\n"
            "N:\tNothing will be updated\n"
            ":\t").upper()
        print("\n")

        # Update the author details of the book
        if should_update == "A":

            # Fetch the current author ID of the book to,
            # Update the author table
            cursor.execute('''
                           SELECT authorID
                           FROM book
                           WHERE id = ?
                           ''', (id,))

            old_authID = cursor.fetchone()
            old_authID = old_authID[0]  # Extract the author ID from the tuple

            # Use a try-except block to catch any ValueError exceptions,
            # Ask user for new author ID
            try:
                update_authorID = int(input(
                    "Enter the correct Author ID : "))
            except ValueError:
                print("\nIncorrect input, only enter the numerical ID.")
                continue  # Will return to the start of the while loop
            print("\n")

            # Update author ID in book table
            cursor.execute('''
                           UPDATE book
                           SET authorID = ?
                           WHERE id = ?
                           ''', (update_authorID, id))

            # Update author ID in author table
            cursor.execute('''
                           UPDATE author
                           SET id = ?
                           WHERE id = ?
                           ''', (update_authorID, old_authID))

            db.commit()

            # Fetch author details to print to user
            cursor.execute('''
                           SELECT *
                           FROM author
                           WHERE id = ?
                           ''', (update_authorID,))

            author_details = cursor.fetchone()

            # Print author details in a friendly format
            print("Author details : \n"
                  f"ID : {author_details[0]}\n"
                  f"Name : {author_details[1]}\n"
                  f"Country : {author_details[2]}\n")

            # Ask user if they want to update,
            # The name and country of the author
            while True:
                update_author = input(
                    "Would you like to update the Authors name and "
                    "country?\n Y/N : ").upper()

                # Ask user for new name and country of the author
                if update_author == "Y":
                    new_name = input(
                        "\nEnter the name of the Author : ").title()
                    new_country = input(
                        "Enter the name of the Author's country of origin"
                        " : ").title()

                    # Update the name and country of the author in the database
                    cursor.execute('''
                                   UPDATE author
                                   SET name = ?, country = ?
                                   WHERE id = ?''',
                                   (new_name, new_country,
                                    update_authorID))

                    db.commit()

                    # Confirmation message that the author details were updated
                    print("\nAuthor details where updated.")
                    break

                elif update_author == "N":
                    break

                # print error message and return to start of,
                # While loop if the input is incorrect
                else:
                    print("\nYour input was incorrect, try again.")

        # Update the title of the book
        # Ask user for the new title of the book
        elif should_update == "T":
            update_title = input(
                "Enter the correct Title of the "
                "book : ").title()

            # Update the title of the book in the database
            cursor.execute('''
                           UPDATE book
                           SET title = ?
                           WHERE id = ?
                           ''', (update_title, id))

            db.commit()
            print("\nTitle updated.")

        # Print a message and return to the main menu
        elif should_update == "N":
            print("Returning to main menu.\n")
            break

        # Print error message for incorrect input and,
        # Return to the start of the while loop
        else:
            print("Incorrect input, please try again.")


def delete_book():
    """
    This function deletes a book from the database using the book ID

    Returns: A confirmation message if the book was deleted successfully.
    """

    # Ask user for the ID of the book they want to delete
    delete_id = input(
        "Enter the ID of the book you want to delete : ").strip()

    # Checks if the input is correct and if it is,
    # Delete the book from the database
    if (len(delete_id) == 4 and delete_id.isdigit()):
        cursor.execute('''DELETE FROM book WHERE id = ?''', (delete_id,))
        db.commit()

        # Confirmation message that the book was deleted.
        print("\nBook was deleted from database.")

    # Error message if the input is not correct and return to the main menu
    else:
        print("\nThe ID entered is incorrect, please try again.")


def search_book():
    """
    This function searches for a book in the database using the book ID

    Returns: The details of the book if it is found.
    """

    # Ask user for the ID of the book they want to search for
    search_id = input(
        "Enter the ID of the book you are looking for : ").strip()

    # Checks if the input is correct
    if (
        len(search_id) == 4
        and search_id.isdigit()
    ):  # If the input is correct, search for the book in the database
        cursor.execute('''SELECT * FROM book
                   WHERE id = ?
                   ''', (search_id,))

        book = cursor.fetchone()

        # Print the details of the book in a friendly format
        if book is not None:
            print(f"""
Book Details:
Book ID :       {book[0]}
Title :         {book[1]}
Author ID :     {book[2]}
Quantity :      {book[3]}""")

        # Error message if the book is not found in the database
        else:
            print("Book not found in the database.")

    # Error message if the input is not correct and return to the main menu
    else:
        print("The ID entered is incorrect, please try again.")


def view_details():
    """
    This function shows the book titles, author names,
    and author countries of all the books in the database.

    Returns: The details of all the books in the database.
    """

    # Fetch the necessary details of all the books in the database
    # Using an inner join
    cursor.execute('''
                   SELECT book.title, author.name, author.country
                   FROM book
                   INNER JOIN author ON book.authorID = author.id
                   ''')

    # Save details in a list of lists
    rows = cursor.fetchall()

    # Print the details of all the books in a friendly format
    print("Details\n")
    print("-" * 50)

    for title, name, country in rows:
        print(f"Title:\t\t\t {title}\n"
              f"Author's name:\t\t {name}\n"
              f"Author's Country:\t {country}")
        print("-" * 50)


def populate_data():
    """
    This function populates the database with the initial data
    provided in the task description.
    """

    # List of book data
    book_data = [
        (3001, "A Tale of Two Cities", 1290, 30),
        (3002, "Harry Potter and the Philosopher's Stone", 8937, 40),
        (3003, "The Lion, the Witch and the Wardrobe", 2356, 25),
        (3004, "The Lord of the Rings", 6380, 37),
        (3005, "Alice's Adventures in Wonderland", 5620, 12),
        (3006, "A Sorceress Comes to Call", 9546, 35),
        (3007, "Percy Jackson and the Lightning Thief", 7856, 12),
    ]

    # List of author data
    author_data = [
        (1290, "Charles Dickens", "England"),
        (8937, "J. K. Rowling", "England"),
        (2356, "C.S. Lewis", "Ireland"),
        (6380, "J.R.R Tolkien", "South Africa"),
        (5620, "Lewis Carroll", "England"),
        (9546, "T. Kingfisher", "Japan"),
        (7856, "Rick Riordan", "USA"),
    ]

    # Insert data into 'book' table
    cursor.executemany(
        '''INSERT INTO book(
        id, title, authorID, qty)
        VALUES (?, ?, ?, ?)
        ''', book_data
    )

    # Insert data into 'author' table
    cursor.executemany(
        '''INSERT INTO author(
        id, name, country)
        VALUES (?, ?, ?)
        ''', author_data
    )


# ------- Create Database --------

# Create path for database file within the same directory as the script
script_dir = Path(__file__).parent
db_path = script_dir / "ebookstore.db"

# Connect to the database and create the tables if they don't exist,
# Using a try-except block to catch any exceptions that may occur
try:
    # Connect to the database
    with sqlite3.connect(db_path) as db:
        cursor = db.cursor()

    # Create 'book' and 'author' tables if they don't exist
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS
        book(id INTEGER PRIMARY KEY,
        title TEXT,
        authorID INTEGER,
        qty INTEGER)'''
    )

    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS
        author(id INTEGER PRIMARY KEY,
        name TEXT,
        country TEXT)'''
    )

    db.commit()

except Exception as e:
    db.rollback()
    print(f"Database error : {e}")

# Populate the database with the initial data
populate_data()
db.commit()

# *********** Menu Section *************

# Print a welcome message to the user
print("Welcome to the Shelf Tracking Database!\n")

# Start an infinite loop to show the menu to the user until they choose to exit
while True:
    while True:
        # Use a while loop to catch any ValueError exceptions that may occur
        try:
            task = int(input("""
Please choose one of the following options:

1.  Enter book
2.  Update book
3.  Delete book
4.  Search book
5.  View details of all books
0.  Exit
:   """))
            break
        except ValueError:
            print("Incorrect input, only type the number.")

    print("\n")

    # Option 1 will add a new book to the database
    if task == 1:

        add_book()
        print("-" * 50)

    # Option 2 will update the book details in the database,
    elif task == 2:

        # Ask user for the ID of the book they want to update
        update_id = input(
            "Enter the ID of the book you want to update : ").strip()

        # Check if the input is correct
        if (
            len(update_id) == 4
            and update_id.isdigit()
        ):
            update_book(update_id)
            print("-" * 50)

        # Error message if the input is not correct and return to the main menu
        else:
            print("The ID entered is incorrect, please try again.")
            print("-" * 50)

    # Option 3 will delete a book from the database
    elif task == 3:

        delete_book()
        print("-" * 50)

    # Option 4 will search for a book in the database and show its details
    elif task == 4:
        search_book()
        print("-" * 50)

    # Option 5 will show the details of all the books in the database
    elif task == 5:
        view_details()

    # Option 0 will exit the program
    elif task == 0:
        print("Thank you for using the Shelf Tracking database.")
        print("Goodbye!")
        break

    # Error message for incorrect input and return to the main menu
    else:
        print("Incorrect input, please try again.")
