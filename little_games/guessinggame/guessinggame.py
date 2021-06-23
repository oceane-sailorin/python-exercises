#guessing computer number

import random

def guessing(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, too low.')
        elif guess > random_number:
            print('Sorry, too high.')

    print(f'Bravo! The number is indeed {random_number}')


guessing(10)