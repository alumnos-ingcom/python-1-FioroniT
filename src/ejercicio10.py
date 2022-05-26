################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def es_palindromo(palabra):
    """
    En esta función se verifica que la palabra es un palindromo y se devuelve un valor lógico
    """
    palindromo = palabra[::-1]
    if palabra == palindromo:
        palabra = True
    else:
        palabra = False
    return palabra
def principal():
    """
    Valor de entrada = palabra (x)
    Valor de salida = valor lógico (True/False)
    """
    palabra =input("Ingrese una palabra para verificar si es un palindromo: ").lower()
    print(es_palindromo(palabra))

if __name__ == "__main__":
    principal()
    
