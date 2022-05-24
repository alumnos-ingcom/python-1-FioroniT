################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def division_lenta(dividendo, divisor):
    """
    Los datos de entrada y salida son números enteros
    """
    dividendo_1 = dividendo
    contador = 0
    while dividendo >= divisor:
        dividendo = dividendo - divisor
        contador += 1
    resto = dividendo_1 - (contador * divisor)
    cociente = contador
    return cociente, resto

def principal():
    dividendo = int(input("Ingrese el dividendo: "))
    divisor = int(input("Ingrese el divisor: "))
    print(f"El cociente y el resto son {division_lenta(dividendo, divisor)}")
    return division_lenta(dividendo, divisor)
    
   
if __name__ == "__main__":
    principal()
    
