tupla = tuple()
tupla = ()

print(type(tupla))

# desta forma a tupla se transforma em string
tupla = ("um")

print(type(tupla))

# o jeito certo para colocar elemento em uma tupla
tupla = ("dois",)

print(type(tupla))

cores = ("verde", "amarelo", "azul", "azul", "azul", "branco")
print(cores[0])
print(cores[-1])
print(cores[1:])

print(cores.index("amarelo"))

print(cores.count("azul"))

print(len(cores))
