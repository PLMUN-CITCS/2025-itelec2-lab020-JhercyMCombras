"""
even_odd_checker_functions.py

This script checks if the user input is even or odd.
It consists of two functions:
1. get_integer_input() - Handles user input and validation.
2. check_even_odd(number) - Checks if the number is even or odd.
"""

def get_integer_input() -> int:
    """
    Prompt the user to enter an integer and validate the input.

    This function repeatedly asks the user for a valid integer input. If the input is not a valid integer,
    it raises an error message and prompts the user again until a valid integer is entered.

    Returns:
        int: The validated integer input by the user.

    Example:
        >>> get_integer_input()
        Enter an integer: 5
        5
    """
    while True:
        try:
            # Ask for user input
            user_input = input("Enter an integer: ")
            number = int(user_input)  # Convert the input to an integer
            return number  # Return the validated integer
        except ValueError:
            # Handle invalid input
            print(f"Error: '{user_input}' is not a valid integer. Please enter a valid integer.")


def check_even_odd(number: int) -> str:
    """
    Determine whether a given integer is even or odd.

    This function checks whether the provided integer is divisible by 2.
    If divisible, it returns a message indicating the number is even; otherwise, it indicates the number is odd.

    Args:
        number (int): The integer to check.

    Returns:
        str: A message indicating if the number is even or odd.

    Example:
        >>> check_even_odd(4)
        '4 is an Even number.'
    """
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."


if __name__ == "__main__":
    # Main program execution
    number = get_integer_input()  # Get valid user input
    result = check_even_odd(number)  # Check if the number is even or odd
    print(result)  # Display the result
