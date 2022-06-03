################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Funciones de conversion de grados a fahrenheit y viceversa
"""
def centigrados_a_fahrenheit(centigrados):
    """
    Los datos de entrada y salida son únicamente grados centigrados
    """
    resultado = (centigrados * 9/5) + 32
    return resultado


def fahrenheit_a_centigrados(fahrenheit):
    resultado = (fahrenheit - 32) * 5/9
    return resultado


def principal():
    """
    Los datos de entrada y salida son únicamente 'int'
    """  
    numero_1 = float(input("Añada cantidad de grados a convertir: "))
    resultado_1 = print(f"{numero_1} C° son {centigrados_a_fahrenheit(numero_1)} F°")
    resultado_2 = print(f"{numero_1} F° son {fahrenheit_a_centigrados(numero_1)} C°")
    return resultado_1, resultado_2


if __name__ == "__main__":
    principal()

