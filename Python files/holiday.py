# Define functions to calculate costs for hotel, plane, car rental, and total holiday cost
def hotel_cost(a):
    """
    Calculates the total cost of the hotel stay.
    
    Parameters: 'a' (int): Number of nights to stay at the hotel.

    Returns: hotel_total (int): Total cost of the hotel stay.
    """
    hotel_total = 900 * a
    return hotel_total

def plane_cost(b):
    """
    Calculates the total cost of the flight.
    Uses a if-else statement to determine the cost based on the chosen cityfrom the 'cities' dictionary.

    Parameters: b (str): The city chosen for the flight.

    Returns: One of the chosen cities (int): Total cost of the flight as predetermined in the cities dictionary.
    """
    if b == "1":
        return cities["New York"]
    elif b == "2":
        return cities["Los Angeles"]
    elif b == "3":
        return cities["Paris"]
    elif b == "4":
        return cities["Bangkok"]

def car_rental(c):
    """
    Calculates the total cost of the car rental.

    Parameters: c (int): Number of days to rent a car.

    Returns: car_total (int): Total cost of the car rental.
    """
    car_total = 150 * c
    return car_total

def holiday_cost(a, b, c):
    """
    Calculates the total cost of the holiday.

    Parameters:
    a: (int): Number of nights to stay at the hotel as specified by user.
    b: (int): City chosen for the flight as determined by the user and corresponds to the dictionary 'cities'.
    c: (int): Number of days to rent a car as specified by the user.

    Returns: holiday_total (int): Total cost of the holiday.
    """
    hotel_total = hotel_cost(a)
    plane_total = plane_cost(b)
    car_total = car_rental(c)
    holiday_total = hotel_total + plane_total + car_total
    return holiday_total

# Create a dictionary containing the cities and their corresponding flight costs
cities = {
    "New York" : 6500, 
    "Los Angeles" : 7500, 
    "Paris" : 5000, 
    "Bangkok": 4500}

# Get user input for city, number of nights, and rental days
city_flight = input("Please choose one of the following cities you want to go to: \n 1.\tNew York,\n 2.\tLos Angeles,\n 3.\tParis,\n 4.\tBangkok \n"
                    "(Type the number of the corresponding city): ")
num_nights = int(input("Please enter the number of nights you would like to stay at the hotel : "))
rental_days = int(input("For how many days would you like to rent a car : "))

# Print the individual costs of the flight, hotel, car rental and the total holiday cost.
print("The cost of the flight will be : " + str(plane_cost(city_flight)))
print("The cost of the hotel will be : " + str(hotel_cost(num_nights)))
print("The cost of the car rental will be : " + str(car_rental(rental_days)))
print("The total cost of the holiday will be : " + str(holiday_cost(num_nights, city_flight, rental_days)))