"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(bt):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    rt = EXPECTED_BAKE_TIME - bt

    return rt
    

#TODO (student): Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.
    
    Parameters:
        number_of_layers (int): The amount of layers in the lasagna.

    Returns:
        int: The amount of time preparing the lasagna.

    This function takes the amount of layers in the lasagna and times it by two, as it takes two minutes to
    make each layer of the lasagna, the it return the amount of time spent preparing the lasagna.
        """
    time = number_of_layers * PREPARATION_TIME

    return time


#TODO (student): define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate elapsed cooking time.

    Parameters:
        number_of_layers (int): The number of layers of the lasagna.
        elapsed_bake_time (int): The time the lasagna has spent baking.

    Return:
        int: The total time spent in the kitchen.

    This function takes two integers, the number of layers of the lasagna and the time spent baking,
    then return the total time spent making the lasagna.
    
    """
    elapsed_time = number_of_layers * 2 + elapsed_bake_time

    return elapsed_time


# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
