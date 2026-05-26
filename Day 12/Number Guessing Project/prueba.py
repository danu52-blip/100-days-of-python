import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 50")

difficulty = input("Choose a difficulty. Type easy or hard: ")

number_random = random.randint(1, 50)
game_over = False

if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

while not game_over and attempts > 0:
    print(f"You have {attempts} attempts remaining.")
    guess = int(input("Make a guess: "))

    if guess > number_random:
        print("Too high")
    elif guess < number_random:
        print("Too low")
    else:
        print("You win!")
        game_over = True
        break

    attempts -= 1

if attempts == 0:
    print("You lose")