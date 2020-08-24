import random

def design(guesses , word):
    if guesses == 0:
        print("--------------") 
        print("|") 
        print("|") 
        print("|") 
        print("|") 
        print("|") 
        print("|") 
        print("|") 
        print("--------------") 

    elif guesses == 1:
        print("--------------") 
        print("|            |") 
        print("|            O") 
        print("|") 
        print("|") 
        print("|") 
        print("|") 
        print("|") 
        print("--------------") 

    elif guesses == 2:
        print("--------------") 
        print("|            |") 
        print("|          \\O") 
        print("|") 
        print("|") 
        print("|") 
        print("|") 
        print("|") 
        print("--------------") 

    elif guesses == 3:
        print("--------------") 
        print("|            |") 
        print("|          \\O/") 
        print("|") 
        print("|") 
        print("|") 
        print("|") 
        print("|") 
        print("--------------") 

    elif guesses == 4:
        print("--------------") 
        print("|            |") 
        print("|          \\O/") 
        print("|            |") 
        print("|") 
        print("|") 
        print("|") 
        print("|") 
        print("--------------") 

    elif guesses == 5:
        print("--------------") 
        print("|            |") 
        print("|          \\O/") 
        print("|            |") 
        print("|           / ") 
        # print("|") 
        print("|") 
        print("|") 
        print("|") 
        print("--------------") 

    elif guesses == 6:
        print("--------------") 
        print("|            |") 
        print("|          \\O/") 
        print("|            |") 
        print("|           / \\ ") 
        # print("|") 
        print("|") 
        print("|") 
        print("|") 
        print("--------------") 
    
        print("\n")
        print("You Lost It.")
        print("The Word is " + word)
        again = input("Do you like to play again(y or n):")
        again = again.lower()
        if again == 'y':
            hangman()
        return
        

def randomword():
    words = random.choice(["police","thief","superman","brick","Program","data","Process","spiderman","ironman"])
    words = words.lower()
    return words

def hangman():
    word = randomword()
    word_list = list(word)
    blanks = "_" * len(word)
    blanks_list = list(blanks)
    new_blank_list = list(blanks)
    guesses = 0
    guess_list = []
    print("Let's Play Hangman\n")
    design(guesses , word)
    print("blanks_list")
    print("Guess The Letter")
    while guesses < len(word):
        guess = input()
        guess = guess.lower()
    # if the player enter more than one letter at a time
        if len(guess) > 1:
            print("Please print only one letter at a time")

    # if player hits enter without writing a letter
        elif len(guess) == 0:
            print("Please enter any one letter")

    # if player repeat a letter that he/she already guess
        elif guess in guess_list:
            print("You have already guessed this letter earlier")
            print("Here is the list of your guesses\n")
            print(guess_list)

    # if player write only one letter and hit enter
        else:
            guess_list.append(guess)
            i = 0
            while i < len(word):
                if guess == word[i]:
                    new_blank_list[i] = word_list[i]
                i = i + 1
            
            # if the guessed letter is not present in the word

            if new_blank_list == blanks_list:
                print("Your word is not here")
                guesses = guesses + 1
                design(guesses,word)

                if guesses < 6:
                    print("guess again")
                    print(blanks_list)

            # if the guessed letter is present in the word

            elif word_list != blanks_list:
                blanks_list = new_blank_list[:]
                print(blanks_list)

                # if the whole world is guess correctly then player wins

                if word_list == blanks_list:
                    print("You Win!!\n")
                    again = input("Do You Want to Play Again(y or n): ")
                    again = again.lower()
                    if again == 'y':
                        hangman()
                    else:
                        quit()

                # if the guesses letter is correct , then tell player to guess again

                else:
                    print("Great Guess, Guess The Next Letter:")

hangman()