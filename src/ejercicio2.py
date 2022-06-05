################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Esta función define el signo de un numero
"""
def signo(numero):
    """
    Los datos de entrada y salida son únicamente int
    """
    if numero == 0:
        resultado = 0
    elif numero > 0:
        resultado = 1
    elif numero < 0:
        resultado = -1
    return resultado


def principal():
    """
    Los valores de entrada y salida son int
    """
    numero = int(input("Ingrese un numero: "))
    (signo(numero))
    salida = (signo(numero))
    print(salida)


if __name__ == "__main__":
    principal()

