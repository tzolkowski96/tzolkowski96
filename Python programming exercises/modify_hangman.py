import random 
 
def hangman(): 
    # Define a list of words to guess
    word_list = ["python", "java", "computer", "hacker", "painter", "photograph", "penguin", "linux", "ubuntu", "windows"] 
    
    # Select a random word from the word list
    random_number = random.randint(0, 9)
    word = word_list[random_number]
    
    # Initialize variables
    wrong = 0 
    stages = ["",
                "________        ",
                "|               ",
                "|        |      ",
                "|        0      ",
                "|       /|\     ",
                "|       / \     ",
                "|               "
                ]
    rletters = list(word)
    board = ["_"] * len(word) 
    win = False 
    print("Welcome to Hangman") 
 
    # Loop until the player wins or loses
    while wrong < len(stages) - 1: 
        print("\n") 
        msg = "Guess a letter: "
        char = input(msg) 
        if char in rletters: 
            # If the player's guess is correct, replace the corresponding underscores with the guessed letter
            cind = rletters.index(char) 
            board[cind] = char 
            rletters[cind] = '$' 
        else: 
            # If the player's guess is incorrect, increment the wrong variable
            wrong += 1 
        print((" ".join(board))) 
        e = wrong + 1 
        print("\n".join(stages[0: e])) 
        if "_" not in board: 
            # If the player has guessed all the letters, print a win message and end the game
            print("You win!") 
            print(" ".join(board)) 
            win = True 
            break
    if not win:
        # If the player has not guessed all the letters, print a lose message and end the game
        print("\n".join(stages[0: wrong])) 
        print("You lose! It was {}.".format(word)) 
 
hangman()