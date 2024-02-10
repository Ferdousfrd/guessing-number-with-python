#The idea is the computer is going to ret a random number and we, users have to guess it

import random

def userGuessGame(range):
    random_number = random.randint(1, range)
    guess = 0

    while guess != random_number:
        guess = int(input("Please make your guess! "))
        if guess > random_number:
             print(f"You have given, {guess}. And random number is smaller than this. Go lower!")
        elif guess < random_number:
            print(f"You have given, {guess}. And random number is bigger than this. Go higher!")
    print(f"Great! You got it right! The random number was {random_number}")

def computerGuessing(x):
    low = 1
    high = x
    decision = ""
    while decision != "c":
        guess = random.randint(low, high)
        decision = input(f"PC guessed, {guess}. If correct, press 'C', if it guessed high then press 'H' and if low then press 'L'__").lower()
        if decision == "h":
            high = guess - 1
        elif decision == "l":
            low = guess + 1

    print("You have guesses correct!")


computerGuessing(10)