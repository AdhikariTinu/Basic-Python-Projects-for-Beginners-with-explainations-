import keyword # To get the list of python keywords

import random # To select a random keyword

name = input("Enter your name here: ") # Taking user name as input

print(f"\nWelcome {name} to the WORD GUESSER. Here you have to guess a puthon keyword within 10 chances.") # Welcoming the user

words = keyword.kwlist # Getting the list of python keywords

word = random.choice(words) # Selecting a random keyword from the list

guess = "" # To store the guessed letters
turn = 10 # Number of turns
print("\nGuess the keyword: ") # Prompting the user to guess the keyword

# print(word) # Uncomment this line to see the selected word for testing purposes

while turn > 0: # Loop until the user runs out of turns
    
    fail = 0 # To count the number of letters not guessed
    
    for ch in word: # Loop through each letter in the word
        
        if ch in guess: # If the letter has been guessed
            print(ch, end="") # Print the letter
        
        else: # If the letter has not been guessed
            print("_", end=" ") # Print an underscore
            fail += 1 # Increment the fail counter
    
    if fail == 0: # If all letters have been guessed
        print(f"\nYou win, and your word is {word}.") # Print the winning message
        break # Exit the loop

    yrw = input("\nEnter your guess: ") # Taking a letter as input from the user
    
    guess += yrw # Adding the guessed letter to the guess string
    
    if yrw not in word:# If the guessed letter is not in the word
        turn -= 1 # Decrement the number of turns
        print(f"\nWrong, you have {turn} more turns to guess the correct word.") # Print the number of turns left

        if turn == 0: # If the user has run out of turns
            print(f"YOU LOST!!, The correct word was {word}.")# Print the losing message    
