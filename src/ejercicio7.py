################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Este programa que permita transformar un número solicitado expresado en grados, minutos y segundos a segundos a segundos.
Y otra que haga el cambio en el sentido contrario, devolviendo una tuple.
"""
def sexadecimal_a_decimal(horas, minutos, segundos):
    """
    Los datos de entrada deben ser numeros positivos
    """
    horas_1 = (horas * 3600)
    minutos_1 = (minutos * 60)
    segundos = segundos
    segundos_1 = (horas_1 + minutos_1 + segundos)
    numero = segundos_1
    return numero


def decimal_a_sexadecimal(numero):
    """
    Los datos de salida deben ser tuple
    """
    tupla_salida = []
    grados = int(numero/3600)
    tupla_salida.append(grados)
    minutos = int((numero-grados*3600)/60)
    tupla_salida.append(minutos)
    segundos = int(numero - (grados*3600)-(minutos*60))
    tupla_salida.append(segundos)
    return tupla_salida


def principal():
    """
    En principal deben entrar 3 numeros, convertirse en uno solo y entrar en la siguiente función para retornar una tupla
    """
    horas = int(input("Indique las horas: "))
    minutos = int(input("Indique los minutos: "))
    segundos = int(input("Indique los segundos: "))
    (sexadecimal_a_decimal(horas, minutos, segundos))
    numero = sexadecimal_a_decimal(horas, minutos, segundos)
    print(numero)
    (decimal_a_sexadecimal(numero))
    salida = (decimal_a_sexadecimal(numero))
    print(salida)


if __name__ == "__main__":
    principal()

