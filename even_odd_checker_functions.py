def get_integer_input() -> int:
    """
    Prompts the user to enter an integer and validates the input.
    
    Returns:
        int: The integer entered by the user.
    
    Raises:
        ValueError: If the input is not a valid integer.
    """
    while True:
        try:
            number = int(input("Enter an integer: "))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number: int) -> str:
    """
    Determines if the given integer is even or odd.
    
    Parameters:
        number (int): The integer to check.
    
    Returns:
        str: A formatted string indicating whether the number is even or odd.
    """
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

if __name__ == "__main__":
    # Get user input
    number = get_integer_input()
    
    # Check if the number is even or odd and display the result
    result = check_even_odd(number)
    print(result)
