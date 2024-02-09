#So the idea is the computer is going to ret a random number and we, users have to guess it

import random

def guessGame(range):
    random_number = random.randint(1, range)
    guess = 0

    while guess != random_number:
        guess = int(input("Please make your guess! "))
        if guess > random_number:
             print(f"You have given, {guess}. And random number is smaller than this. Go lower!")
        elif guess < random_number:
            print(f"You have given, {guess}. And random number is bigger than this. Go higher!")
    print(f"Great! You got it right! The random number was {random_number}")

guessGame(10)