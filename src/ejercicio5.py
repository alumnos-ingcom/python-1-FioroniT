################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
En este programa se hace una división mediante restas consecutivas
"""
def division_lenta(dividendo, divisor):
    """
    Los datos de entrada y salida son números enteros
    """
    dividendo_1 = dividendo
    cociente = 0
    dividendo_abs = abs(dividendo)
    divisor_abs = abs(divisor)
    signo_dividendo = dividendo // dividendo_abs
    signo_divisor = divisor // divisor_abs
    while dividendo_abs >= divisor_abs:        
        dividendo_abs = dividendo_abs - divisor_abs
        cociente += signo_dividendo // signo_divisor
    resto = dividendo_1 - (cociente * divisor)
    return cociente, resto
def principal():
    """
    Los datos de entrada y salida son números enteros
    """
    dividendo = (int(input("Ingrese el dividendo: ")))
    divisor = (int(input("Ingrese el divisor: ")))
    print(division_lenta(dividendo, divisor)) 
    
   
if __name__ == "__main__":
    principal()
