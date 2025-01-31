################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Esta función verifica que la palabra es un palindromo y devuelve un bool
"""
def es_palindromo(texto):
    """
    Esta función toma una str y devuelve un bool
    """
    i = 0
    palindromo = False
    largo = len(texto)
    while i < largo:
        if texto[i] == texto[largo - (i + 1)]:
            i = i + 1
        else:
            i = largo + 5
    if i == largo:
        palindromo = True
    else:
        palindromo = False
    return palindromo


def principal():
    """
    Valor de entrada = palabra (str)
    Valor de salida = valor lógico (True/False)
    """
    texto = input("Ingrese una palabra: ").lower()
    (es_palindromo(texto))
    salida = (es_palindromo(texto))
    print(salida)


if __name__ == "__main__":
    principal()

