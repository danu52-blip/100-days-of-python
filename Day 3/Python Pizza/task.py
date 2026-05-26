print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "s":
    bill = 15
    if pepperoni == "y":
        bill += 2
    if extra_cheese == "y":
        bill += 1
    print (f"You must to pay: $ {bill}")

if size == "m":
    bill = 20
    if pepperoni == "y":
        bill += 3
    if extra_cheese == "y":
        bill += 1
    print(f"You must to pay: $ {bill}")

if size == "l":
    bill = 25
    if pepperoni == "y":
        bill += 3
    if extra_cheese == "y":
        bill += 1
    print(f"You must to pay: $ {bill}")
