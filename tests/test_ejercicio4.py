################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio4 import suma_lenta

"""
En este test se va a probar la funcionalidad del programa de suma lenta de dos números
"""
def test_suma_lenta_positivos():
    numero = 4
    otro_numero = 3
    resultado = suma_lenta(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser un número de tipo entero"
    assert resultado == (4 + 1
                        5
                        5 + 1
                        6
                        6 + 1
                        7),"La suma debe hacerse dígito por dígito"
def test_suma_lenta_negativos():
    numero = -4
    otro_numero = -3
    resultado = suma_lenta(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser un número de tipo entero"
    assert resultado == (4 - 1
                        3
                        3 - 1
                        2
                        2 - 1
                        1), "La resta debe hacerse dígito por dígito"
    