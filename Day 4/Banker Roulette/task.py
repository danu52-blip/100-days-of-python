import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

nombre_random = random.choice(friends)
print(nombre_random)

index_random = random.randint(0,4)
print(friends[index_random])