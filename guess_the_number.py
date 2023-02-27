

# This is a guess the number game

import random

new_request = True
while new_request:

    guesses_taken = 0

    name = input("Hey, What is your name?\n")

    number = random.randint(1, 25)

    print(f"Hello, {name}, I'm thinking of a number between 1 and 25, What could that number be?")

    for guesses_taken in range(8):
        guess = input("Take a guess\n")
        guess = int(guess)

        if guess > number:
            print("The number is too high")

        if guess < number:
            print("The number is too low")

        if guess == number:
            break

    if guess == number:
        guesses_taken = str(guesses_taken + 1)
        print(f"Good job {name}, You guessed the right number in {guesses_taken} guesses!")

    if guess != number:
        number = str(number)
        print(f"Nope! The number I was thinking of was {number}")

    user_response = input("Do you want to play again?(yes or no)")

    if user_response == "no":
        print("Thank you for playing")
        new_request = False
