<<<<<<< HEAD
def get_integer_input() -> int:
    """
    Prompt the user to enter a valid integer.
=======
"""
even_odd_checker_functions.py

This part tell if the user input is even or odd
It consists two functions:
1. get_integer_input() - Handle user input and validation.
2. check_even_odd(number) - check if the number is even or odd.
"""

def get_integer_input() -> int:
    """
    Ask the user to enter a valid integer.
>>>>>>> 816704a8e087b50a64cd4f2ca6c0c140ef53d09a

    Returns:
        int: The validated integer input by the user.
    """
    while True:
        try:
<<<<<<< HEAD
            number = int(input("Enter an integer: "))
            return number
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")
=======
            number = int(input("Enter an integer: "))  # User input
            return number  # Return the validated integer
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")  # check non-integer input
>>>>>>> 816704a8e087b50a64cd4f2ca6c0c140ef53d09a


def check_even_odd(number: int) -> str:
    """
    Determine whether a given number is even or odd.

    Args:
        number (int): The integer to check.

    Returns:
        str: A message indicating if the number is even or odd.
    """
    if number % 2 == 0:
<<<<<<< HEAD
        return f"{number} is an Even number."
    return f"{number} is an Odd number."


if __name__ == "__main__":
    # Get user input and display the result
    user_number = get_integer_input()
    result = check_even_odd(user_number)
    print(result)
def get_integer_input():

    while True:
        try:
            number = int(input("Enter an integer: "))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number):

    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."


number = get_integer_input()
result = check_even_odd(number)
print(result)
=======
        return f"{number} is an Even number."  # Return message for even number
    return f"{number} is an Odd number."  # Return message for odd number


if _name_ == "_main_":
    # Main program execution
    user_number = get_integer_input()  # Get user input
    result = check_even_odd(user_number)  # Check even/odd status
    print(result)  # Display the result
>>>>>>> 816704a8e087b50a64cd4f2ca6c0c140ef53d09a
