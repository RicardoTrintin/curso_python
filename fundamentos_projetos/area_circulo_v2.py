
def circulo(raio):
    pi = 3.1415
    result = pi * float(raio) ** 2
    print("Area da circulo: ", result)


if __name__ == "__main__":
    raio = input("Informe o raio: ")
    circulo(raio)
