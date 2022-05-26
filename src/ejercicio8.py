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
    divisor = 1
    primo = 0
    while divisor < numero:
        divisor = divisor+1
        if numero % divisor != 0:
            primo = 1
        else:
            primo = 0
            if primo == 1:
                primo = True
            else:
                primo = False
    return primo

def principal():
    """
    Los datos de entrada son números y la salida es un valor lógico
    """

    numero = int(input("Ingrese un número para verificar si es primo: "))
    es_primo(numero)
    

if __name__ == "__main__":
    principal()
