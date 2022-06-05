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
    """
    Esta toma como dato de entrada una temperatura en grados y retorna el valor en fahrenheit
    """
    resultado = (fahrenheit - 32) * 5/9
    return resultado


def principal():
    """
    Los datos de entrada y salida son únicamente 'int'
    """  
    centigrados = float(input("Añada cantidad de C° a convertir: "))
    fahrenheit = float(input("Añada cantidad de F° a convertir: "))
    centigrados_a_fahrenheit(centigrados)
    fahrenheit_a_centigrados(fahrenheit)
    print(f"{centigrados} C° son {centigrados_a_fahrenheit(centigrados)} F°")
    print(f"{fahrenheit} F° son {fahrenheit_a_centigrados(fahrenheit)} C°")


if __name__ == "__main__":
    principal()

