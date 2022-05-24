################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def suma_lenta(numero, otro_numero):
    """
    Los datos de entrada y salida deben ser numeros
    """
    for i in range(otro_numero):
        print(f"{numero} + 1")
        numero = numero + 1
        print(numero)
    return numero
   
   
def principal():
    numero = int(input("Ingrese el primer numero: "))
    otro_numero = int(input("Ingrese el segundo numero: "))
    suma_lenta(numero, otro_numero)
   
if __name__ == "__main__":
    principal()

