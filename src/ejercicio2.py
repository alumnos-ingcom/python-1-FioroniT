################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def signo(numero):
    """
    Los datos de entrada y salida son únicamente números enteros
    """
    if numero == 0:
        resultado = 0
    elif numero > 0:
        resultado = 1
    elif numero < 0:
        resultado = -1
    return resultado


def principal():
    numero = int(input("Ingrese un numero: "))
    print(signo(numero))
   
if __name__ == "__main__":
    principal()
