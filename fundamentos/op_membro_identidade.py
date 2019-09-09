list = [1, 2, 3, "Ana", "Maria"]

print(2 in list)
print("Ana" in list)
print(5 in list)

x = 3
y = x
z = 3

print(x is y)
print(y is z)
print(z is not z)

list_a = [1, 2, 3]
list_b = list_a
list_c = [1, 2, 3]

# será igual a lista A pois estao compartilhando o mesmo espaço de memoria
print(list_a is list_b)
# não será igual a lista A pois nao ocupam o mesmo espaço de memoria
print(list_b is list_c)

print(list_a is not list_c)
