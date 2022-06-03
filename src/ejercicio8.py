################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Los datos de entrada son números y la salida es un valor lógico
"""
def es_primo(numero):
    """
    Los datos de entrada son números y la salida es un valor lógico
    """
    divisor = 2
    while divisor < numero:
        if numero % divisor == 0:
            return False
        divisor = divisor + 1
    return True


def principal():
    """
    Los datos de entrada son números y la salida es un valor lógico
    """
    numero = int(input("Ingrese un número para verificar si es primo: "))
    es_primo(numero)


if __name__ == "__main__":
    principal()

