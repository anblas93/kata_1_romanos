from roman_numbers import *

class RomanNumber:
    def __init__(self, entrada):
        if type(entrada) == int:
            self._numero = entrada
            self._simbolo = entero_a_romano(entrada)
        elif type(entrada) == str:
            self._numero = romano_a_entero(entrada)
            self._simbolo = entrada
        else:
            raise RomanNumberError('Debe inicializarse con un entero o romano válido')

    @property()
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, entrada):
        self._numero = entrada
        self._simbolo = entero_a_romano(entrada)