#TODO-1
#Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

import random

word_list = ["Hola", "Chau", "Manzana", "Mate"]
chosen_word = random.choice(word_list)
print(chosen_word)

#TODO-2
#Ask the user to guess a letter and assign their answer to a variable called guess.
#Make the String stored in guess lowercase.

#Search Google for the lower() function in Python.

guess = input("Guess a letter: ").lower()

#TODO-3
#Check if the letter the user guessed guess is one of the letters
#in the chosen_word. Loop through each of the letters
#in the chosen_word and print "Right" if the letter is a match, "Wrong" if it's not.

for char in chosen_word:
    if char == guess:
        print("Right")
    else:
        print("Wrong")
