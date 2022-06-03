################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Los datos de entrada y salida deben ser números enteros
"""
def ordenar_mayor_a_menor(uno, dos, tres):
    """
    Los datos de entrada y salida deben ser números enteros
    """
    if uno > dos and uno > tres:
        if dos > tres:
            tupla_mayor = (f"{uno}", f"{dos}", f"{tres}")
        else:
            tupla_mayor = (f"{uno}", f"{tres}", f"{dos}")
    elif uno > dos and uno < tres:
        tupla_mayor = (f"{tres}", f"{uno}", f"{dos}")
    elif uno < dos and dos < tres:
        tupla_mayor = (f"{tres}", f"{dos}", f"{uno}")
    elif uno < dos and uno > tres:
        tupla_mayor = (f"{dos}", f"{uno}", f"{tres}")
    elif uno < dos and uno < tres:
        tupla_mayor = (f"{dos}", f"{tres}", f"{uno}")
    return tupla_mayor
def ordenar_menor_a_mayor(uno, dos, tres):
    """
    Los datos de entrada y salida deben ser números enteros
    """
    if uno < dos and uno < tres:
        if dos < tres:
            tupla_menor = (f"{uno}", f"{dos}", f"{tres}")
        else:
            tupla_menor = (f"{uno}", f"{tres}", f"{dos}")
    elif uno < dos and uno > tres:
        tupla_menor = (f"{tres}", f"{uno}", f"{dos}")
    elif uno > dos and dos > tres:
        tupla_menor = (f"{tres}", f"{dos}", f"{uno}")
    elif uno > dos and uno < tres:
        tupla_menor = (f"{dos}", f"{uno}", f"{tres}")
    elif uno < dos and dos > tres:   
        tupla_menor = (f"{dos}", f"{tres}", f"{uno}")
    return tupla_menor
def principal():
    """
    Los datos de entrada y salida deben ser números enteros
    """
    uno = int(input("Inserte número 1: "))
    dos = int(input("Inserte número 2: "))
    tres = int(input("Inserte número 3: "))
    print(ordenar_mayor_a_menor(uno, dos, tres))
    print(ordenar_menor_a_mayor(uno, dos, tres))   
if __name__ == "__main__":
    principal()

