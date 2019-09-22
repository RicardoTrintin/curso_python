lista = []
type(lista)
dir(lista)
lista.append(1)
lista.append(5)
print(lista)
print(len(lista))

nova_lista = [1, 5, "Ana", "Bia"]
print(nova_lista)
nova_lista.remove(5)
print(nova_lista)
nova_lista.reverse()
print(nova_lista)

nova_lista2 = [1, 5, "Rebeca", "Guilherme", 3.1415]
print(nova_lista2.index("Guilherme"))
print(nova_lista2[2])
print(1 in nova_lista2)
print("Rebeca" in nova_lista2)
print("Pedro" not in nova_lista2)
print(nova_lista2[0])
print(nova_lista2[4])
print(nova_lista2[-1])
print(nova_lista2[-5])

nova_lista3 = ["Ana", "Lia", "Rui", "Paulo", "Dani"]
print(nova_lista3[1:3])
print(nova_lista3[1:-1])
print(nova_lista3[1:])
print(nova_lista3[:-1])
print(nova_lista3[:])
print(nova_lista3[::2])
print(nova_lista3[::-1])
del nova_lista3[2]
print(nova_lista3)

del nova_lista3[1:]
print(nova_lista3)

