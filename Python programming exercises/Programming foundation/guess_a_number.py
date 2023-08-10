# Define a list of numbers to guess
numbers = [10, 25, 42, 56, 73]
 
# Loop until the user quits
while True: 
    # Prompt the user to guess a number or quit
    guess = input("Guess a number or type 'q' to quit: ")
    
    # If the user quits, end the game
    if guess.lower() == 'q':
        print("Thank you for playing!")
        break 
 
    try: 
        # Try to convert the user input to an integer
        guess = int(guess)
        
        # Check if the user's guess is in the list of numbers
        if guess in numbers:
            print("You guessed correctly!")
        else: 
            print("You guessed incorrectly! Try again!")
    except ValueError:
        # If the user input cannot be converted to an integer, print an error message
        print("Please enter an integer or type 'q' to quit.")