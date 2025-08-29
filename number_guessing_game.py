import random
print(f"\nWelcome to the NUMBER guessing game. Please select your lower and upper bound below.")

num1 = int(input(f"\n Please select your lower bound: "))
num2 = int(input(f"\n Please select your upper bound: "))

print(f"\n You have 7 guesses to find the number between {num1} and {num2}.Let's begin! \n")

r_no = random.randint(num1, num2)
g = 0
ch = 7

while g < ch:
    g += 1
    guess = int(input(f"\n Enter your guess no. {g}: "))

    if guess == r_no:
        print(f"\n Hurray!,You guessed the right no. that is {r_no}. And guessed it in {g} attempt(s)")
        break
    elif g >= ch and guess != r_no:
        print(f"\n Sorry, Your number was {r_no}, Better luck next time")

    elif guess > r_no:
        print(f"\n Your number is lower than this!")

    elif guess < r_no:
        print(f"\n Your number is higher than this!")