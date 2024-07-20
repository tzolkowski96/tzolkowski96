# create_a_module.py

# Import the calculate_cube function from the cubed module
from cubed import calculate_cube

def main():
    """
    Main function to demonstrate the usage of calculate_cube function.
    """
    try:
        # Call the calculate_cube function with an argument of 2 and store the result in the result variable
        result = calculate_cube(2)
        
        # Print the result of the calculate_cube function
        print(f"The cube of 2 is: {result}")  # Output: 8
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
