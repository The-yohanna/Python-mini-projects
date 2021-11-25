import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry you have guessed wrong. Too low!")
        elif guess > random_number:
            print("Sorry you have guessed wrong. Too high!")

    print(f"Yay, you have guessed right the number {random_number} congrats!!")

guess(20)