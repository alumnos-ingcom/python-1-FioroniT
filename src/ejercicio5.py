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
    dividendo = abs(int(input("Ingrese el dividendo: ")))
    divisor = abs(int(input("Ingrese el divisor: ")))
    print(division_lenta(dividendo, divisor)) 
    
   
if __name__ == "__main__":
    principal()