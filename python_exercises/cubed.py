# cubed.py

def calculate_cube(num):
    """
    Calculate the cube of a number.

    Parameters:
    num (int or float): The number to be cubed.

    Returns:
    int or float: The cube of the input number.
    """
    if not isinstance(num, (int, float)):
        raise TypeError("Input must be an integer or float")
    return num ** 3
