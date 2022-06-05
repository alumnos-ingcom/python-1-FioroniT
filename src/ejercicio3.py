################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Esta función compara dos numeros e indica cual es mayor o si son iguales
"""
def compara(numero, otro_numero):
    """
    Los datos de entrada y salida deben ser números enteros
    """
    if numero > otro_numero:
        resultado = 1
    elif numero < otro_numero:
        resultado = -1
    else:
        resultado = 0
    return resultado


def principal():
    """
    Los datos de entrada y salida deben ser int
    """
    numero = int(input("Ingrese número 1: "))
    otro_numero = int(input("Ingrese número 2: "))
    (compara(numero, otro_numero))
    salida = (compara(numero, otro_numero))
    print(salida)
    

if __name__ == "__main__":
    principal()

