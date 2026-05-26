MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def check_resources(choice):
    for ingredient in MENU[choice]["ingredients"]:
        amount_needed = MENU[choice]["ingredients"][ingredient]
        if resources[ingredient] < amount_needed:
            return ingredient
    return None


def check_payment(payment, cost):
    difference = payment - cost
    if difference < 0:
        return "insufficient"
    return difference  # 0 or positive


def make_coffee(choice):
    for ingredient in MENU[choice]["ingredients"]:
        resources[ingredient] -= MENU[choice]["ingredients"][ingredient]


machine_on = True

while machine_on:

    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        machine_on = False

    elif choice == "report":
        print_report()

    elif choice in MENU:

        missing_ingredient = check_resources(choice)

        if missing_ingredient is not None:
            print(f"Sorry, there is not enough {missing_ingredient}.")
        else:
            payment = float(input("Insert money: $"))
            payment_result = check_payment(payment, MENU[choice]["cost"])

            if payment_result == "insufficient":
                print("Sorry, that's not enough money. Money refunded.")
            else:
                if payment_result > 0:
                    print(f"Here is your change: ${payment_result:.2f}")

                resources["money"] += MENU[choice]["cost"]
                make_coffee(choice)
                print(f"Here is your {choice}. Enjoy!")

    else:
        print("Invalid option.")
