name = input("Ingresa tu nombre: ")
last_name = input("Ingresa tu apellido: ")

def format_name(f_name, l_name):
    result= (name + " " + last_name).title()
    print(result)

format_name(f_name=name, l_name=last_name)


