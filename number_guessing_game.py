# A number guessing game where the user has to guess a randomly generated number within a specified range and a limited number of attempts.
import random # importing random module to generate random numbers
print(f"\nWelcome to the NUMBER guessing game. Please select your lower and upper bound below.") # Welcoming the user

num1 = int(input(f"\n Please select your lower bound: ")) # Taking lower bound input from user
num2 = int(input(f"\n Please select your upper bound: ")) # Taking upper bound input from user

print(f"\n You have 7 guesses to find the number between {num1} and {num2}.Let's begin! \n") # Informing the user about the number of attempts

r_no = random.randint(num1, num2) # Generating a random number between the specified bounds
g = 0                             # Initializing guess counter
ch = 7                            # Setting the maximum number of attempts

# Loop until the user has exhausted their attempts
while g < ch: # Looping until the user has exhausted their attempts
    g += 1    # Incrementing the guess counter
    guess = int(input(f"\n Enter your guess no. {g}: ")) # Taking the user's guess as input

    if guess == r_no:  # Checking if the guess is correct
        print(f"\n Hurray!,You guessed the right no. that is {r_no}. And guessed it in {g} attempt(s)") # Congratulating the user for the correct guess
        break # Exiting the loop if the guess is correct
    elif g >= ch and guess != r_no: # Checking if the user has exhausted their attempts
        print(f"\n Sorry, Your number was {r_no}, Better luck next time") # Informing the user that they have exhausted their attempts

    elif guess > r_no: # Checking if the guess is too high
        print(f"\n Your number is lower than this!") # Giving a hint that the guess is too high

    elif guess < r_no: # Checking if the guess is too low
        print(f"\n Your number is higher than this!") # Giving a hint that the guess is too low