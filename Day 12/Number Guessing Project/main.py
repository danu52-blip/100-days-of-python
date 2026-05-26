import art
import random

print(art.logo)
print("Welcome to the Number Guessing Name!")
print("I'm thinking of a number between 1 and 50")
dificulty = input("Choose a dificulty. Type easy or hard: ")

numbers = list(range(1, 50))
number_random = random.choice(numbers)
game_over = False

attempts_easy = 10
while not game_over:

    if dificulty == "easy":
        print(f"You have {attempts_easy} attempts remaining to guess the number. ")
        guess = int(input("Make a guess: "))

        if guess > number_random:
            print("Too high")
        elif guess < number_random:
            print("Too low")
        else:
            print("You win!")
            game_over = True

    attempts_easy -= 1

    if attempts_easy == 0:
        game_over = True
        print("You lose")


attempts_hard = 5
while not game_over:

    if dificulty == "hard":
        print(f"You have {attempts_hard} attempts remaining to guess the number. ")
        guess = int(input("Make a guess: "))

        if guess > number_random:
            print("Too high")
        elif guess < number_random:
            print("Too low")
        else:
            print("You win!")
            game_over = True

    attempts_hard -= 1

    if attempts_hard == 0:
        game_over = True
        print("You lose")

