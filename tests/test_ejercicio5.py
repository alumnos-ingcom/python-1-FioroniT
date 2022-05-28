################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio5 import division_lenta
"""
Esta funcion realiza una división a partir de restas lentas
"""
def test_division_lenta():
    dividendo = 10
    divisor = 3
    resultado = division_lenta(dividendo, divisor)
    assert isinstance(resultado, tuple)
    assert resultado == (3, 1)