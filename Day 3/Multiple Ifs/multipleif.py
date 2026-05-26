print("Welcome to the rollercoaster!")
height = int(input("What is your heigh in on? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child ticket are $5")
    elif age <= 18:
        bill = 7
        print("Youth ticket are $7")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Entra gratis")
    else:
        bill = 12
        print("Adult ticket are $12")

    wants_photo = input("Do you want have a photo take? Tape Y or N ")
    if wants_photo == "Y":
        bill += 3

    #No pongo ningun else porque se supone que si ponen que no, entonces no tengo que hacer nada, solo imprimir la factura
    print(f"Your final bill is $ {bill}")

else: 
    print("Sorry, you can't ride the rollercoaster")
