################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def es_palindromo(texto):
    """
    En esta función se verifica que la palabra es un palindromo y se devuelve un valor lógico
    """
    palindromo = texto[::-1]
    if texto == palindromo:
        texto = True
    else:
        texto = False
    return texto
def principal():
    """
    Valor de entrada = palabra (x)
    Valor de salida = valor lógico (True/False)
    """
    texto = input("Ingrese una palabra para verificar si es un palindromo: ").lower()
    print(es_palindromo(texto))

if __name__ == "__main__":
    principal()
    
