from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_images[dice_num])


#NO EMPIEZA DESDE EL 1 EL RANGO, PORQUE LOS "INDEX" EMPIEZAN A CONTAR DESDE 0
#QUE SERIA LA PRIMERA POSICION, ENTONCES EL 1 NUNCA LO TIENE EN CUENTA. EL RANGO DEBE SER 0,5