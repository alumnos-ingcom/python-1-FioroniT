################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Esta función debe sumar dos números indicados de manera lenta
"""
def suma_lenta(numero, otro_numero):
    """
    Los datos de entrada y salida deben ser int
    """
    if otro_numero > 0:
        for i in range(otro_numero):
            numero = numero + 1
    elif otro_numero < 0:
        otro_numero = otro_numero * -1
        for i in range(otro_numero):
            numero = numero - 1
    return numero


def principal():
    """
    Los valores de  entrada y salida son int
    """
    numero = int(input("Ingrese el primer numero: "))
    otro_numero = int(input("Ingrese el segundo numero: "))
    suma_lenta(numero, otro_numero)
    salida = suma_lenta(numero, otro_numero)
    print(salida)


if __name__ == "__main__":
    principal()

