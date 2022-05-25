################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Los datos de entrada deben ser numeros positivos
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
    Los datos de entrada deben ser numeros positivos
    """
    grados = int(numero/3600)
    minutos = int((numero-grados*3600)/60)
    segundos = int(numero - (grados*3600)-(minutos*60))
    return (f"{grados}", f"{minutos}", f"{segundos}")   
def principal():
    """
    Los datos de entrada deben ser numeros positivos
    """
    horas=int(input("Indique las horas: "))
    minutos=int(input("Indique los minutos: "))
    segundos=int(input("Indique los segundos: "))
    numero=sexadecimal_a_decimal(horas, minutos, segundos)
    print(sexadecimal_a_decimal(horas, minutos, segundos))
    print(decimal_a_sexadecimal(numero))

if __name__ == "__main__":
    principal()

