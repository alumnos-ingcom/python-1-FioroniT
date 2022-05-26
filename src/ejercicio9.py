################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Los valores de entrada y salida deben ser numeros,
especificamente los de salida deben coincidir con los factores primos del numero de entrada
"""
def factores_primos(numero):
    """
    Valor de entrada = número (x) entero
    Valor de salida = factores primos de (x)
    """
    lista = []
    divisor = 2
    while numero > 1:
        if numero % divisor == 0:
            numero = numero // divisor
            lista.append(divisor)
        else:
            divisor = divisor + 1
    tupla_factores = tuple(lista)
    return tupla_factores  
def principal():
    """
    Valor de entrada = número (x) entero
    Valor de salida = factores primos de (x)
    """
    numero = int(input("Ingrese un número para verificar sus factores primos: "))
    print(factores_primos(numero))

if __name__ == "__main__":
    principal()
