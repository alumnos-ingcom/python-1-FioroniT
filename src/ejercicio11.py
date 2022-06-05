################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
En esta función los valores de entrada y salida serán int
"""
def es_multiplo(numero, multiplo):
    """
    Esta función evalúa si el segundo número indicado es múltiplo del segundo
    """
    retorno = None
    while multiplo >= numero:
        multiplo = multiplo - numero
    if multiplo == 0:
        retorno = True
    else:
        retorno = False
    return retorno

def principal():
    """
    Valores de Entrada: Numeros enteros
    Valores de Salida: Booleanos
    """
    numero = abs(int(input("Ingrese un numero: ")))
    multiplo = abs(int(input("Ingrese un multiplo: ")))
    print(es_multiplo(numero, multiplo))


if __name__ == "__main__":
    principal()

