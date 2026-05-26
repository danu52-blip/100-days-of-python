import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def substract(n1,n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+":add,
    "-":substract,
    "*":multiply,
    "/":divide,
}

#print(operations ["*"](8,4))

def calculator():
    should_acumulate = True
    f_number = int(input("Type the first number: "))

    while should_acumulate:
            for symbol in operations:
                print(symbol)
            operator = input("Type a mathematical operator: + , - , * , / : ")
            s_number = int(input("Type the second number: "))
            answer = operations[operator](f_number, s_number)
            print(f"{f_number} {operator} {s_number} = {answer}")


            choice = input(f"Do you want to continue with the result {answer}? yes or no?: ")
            if choice == "yes":
                f_number = answer

            else:
                should_acumulate = False
                print("\n" *20)
                print(art.logo)
                calculator()

calculator()