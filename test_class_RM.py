'''
from cromannumbers import RomanNumber

def test_instanciar_un_numero_romano():
    romano = RomanNumber(23)
    assert romano.numero == 23
    assert romano._simbolo == 'XXIII'

def test_instanciar_otro():
    romano = RomanNumber(13)
    assert romano.numero == 13
    assert romano._simbolo == 'XIII'

def test_instanciar_con_simbolo():
    romano = RomanNumber('XI')
    assert romano.numero == 11
    assert romano._simbolo == 'XI'

def test_cambiar_el_valor():
    romano = RomanNumber(1)
    assert romano.numero == 1
    assert romano._simbolo == 'I'

    romano.numero = 2
    assert romano.numero == 2
    assert romano._simbolo == 'II'
    '''

class Alumna:
    def __init__(self, n, a):
        self.nombre = n
        self.apellido = a

def test_irene_existe():
    angel = Alumna("Angel", "Fariñas")
    assert angel.nombre == "Angel"
    assert angel.apellido == "Fariñas"