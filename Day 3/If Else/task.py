print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the Rollercoaster!")
    age = int(input("How old are you? "))
    if age < 12:
        bill = 5
        print("The ticket is $5")
    elif age >= 12 and age <= 18:
        bill = 7
        print("The ticket is $7")
    else:
        bill = 12
        print("The ticket is $12")
    wants_photo = input ("Do you want a photo? type y or n: ")
    if wants_photo == "y":
        bill += 3
    print(f"You must pay $ {bill}")
else:
    print("Sorry, you can't ride yet.")