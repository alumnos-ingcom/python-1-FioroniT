################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Para esta función los valores de entrada y salida serán únicamente números enteros
"""
def es_multiplo(numero, multiplo):
    """
    Esta función evalúa si el segundo número indicado es múltiplo del segundo
    """
    while multiplo >= numero:
        multiplo = multiplo - numero
    if multiplo == 0:
        return True
    else:
        return False
def principal():
    """
    Valores de Entrada y Salida: Numeros enteros
    """
    numero = int(input("Ingrese un numero: "))
    multiplo = int(input("Ingrese un multiplo: "))
    print(es_multiplo(numero, multiplo))
   
if __name__ == "__main__":
    principal()
   
