import sys
import errno


class TerminalColor:
    ERRO = "\033[91m"
    NORMAL = "\033[0m"


def circulo(raio):
    pi = 3.1415
    result = pi * float(raio) ** 2
    return result


def help():
    print("Area da circulo: ", area)
    print("Area da circulo: {} <raio>".format(sys.argv[0]))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raio = input("Informe o raio: ")
        area = circulo(raio)
        help()
    elif not sys.argv[1].isnumeric():
        print(TerminalColor.ERRO + "Parametro nao suportado" +
              TerminalColor.NORMAL)
        sys.exit(errno.EINVAL)
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print("Area da circulo: ", area)
