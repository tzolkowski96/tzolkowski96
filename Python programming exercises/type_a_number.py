# Define a function that converts user input to an integer
def num_converter():
    # Prompt the user to type a number
    user_input = input("Type a number: ")
    try: 
        # Try to convert the user input to an integer
        user_input = int(user_input)
        # Print the integer value of the user input
        print(user_input)
    except:
        # If the user input cannot be converted to an integer, print an error message
        print("Please type an integer.")