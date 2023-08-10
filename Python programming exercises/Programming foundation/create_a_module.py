# Define a function that calculates the cube of a number
def calculate_cube(num):
    return num ** 3

# Import the calculate_cube function from the cubed module
from cubed import calculate_cube

# Call the calculate_cube function with an argument of 2 and store the result in the result variable
result = calculate_cube(2)

# Print the result of the calculate_cube function
print(result) # Output: 8