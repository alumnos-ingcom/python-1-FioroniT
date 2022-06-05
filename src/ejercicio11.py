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
        retorno = multiplo == 0
    return retorno

def principal():
    """
    Valores de Entrada: Numeros enteros
    Valores de Salida: Booleanos
    """
    numero = abs(int(input("Ingrese un numero: ")))
    multiplo = abs(int(input("Ingrese un multiplo: ")))
    (es_multiplo(numero, multiplo))
    salida = (es_multiplo(numero, multiplo))
    print(salida)


if __name__ == "__main__":
    principal()

