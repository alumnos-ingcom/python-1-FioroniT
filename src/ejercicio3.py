################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################

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
    
    """
    numero = int(input("Ingrese número 1: "))
    otro_numero = int(input("Ingrese número 2: "))
    print(compara(numero, otro_numero))
if __name__ == "__main__":
    principal()

