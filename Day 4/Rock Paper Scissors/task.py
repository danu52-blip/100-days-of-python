import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for rock, 1 for Paper, 2 for Scissors: "))
images = [rock, paper, scissors]

if user_choice >= 3 or user_choice <0:
    print("Invalid number. You lose")

else:
    print(images[user_choice])

    computer_choice = random.randint(0,2)
    print("Computer chosen")
    print(images[computer_choice])

    if user_choice == computer_choice:
        print("It's a draw")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose")









