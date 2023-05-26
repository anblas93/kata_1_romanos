from roman_numbers import romano_a_entero, RomanNumberError
import pytest # Para testear excepciones

def test_simbolos():
    assert romano_a_entero('I') == 1
    assert romano_a_entero('L') == 50

def test_sumando():
    assert romano_a_entero('CXXIII') == 123


def test_resta_normal():
    assert romano_a_entero('IV') == 4
    assert romano_a_entero('IX') == 9

def test_composicion_numero():
    assert romano_a_entero('MMCMXLIX') == 2949

def test_no_mas_3_repeticiones():
    with pytest.raises(RomanNumberError):
        romano_a_entero('CCCC')

def test_de_no_repetir_VLD():
    with pytest.raises(RomanNumberError):
        romano_a_entero('VV')
    with pytest.raises(RomanNumberError):
        romano_a_entero('LL')
    with pytest.raises(RomanNumberError):
        romano_a_entero('DD')

def test_restas_permitidas():
    with pytest.raises(RomanNumberError):
        romano_a_entero('IC')
    with pytest.raises(RomanNumberError):
        romano_a_entero('IL')
    with pytest.raises(RomanNumberError):
        romano_a_entero('XD')
    with pytest.raises(RomanNumberError):
        romano_a_entero('XM')   

    with pytest.raises(RomanNumberError):
        romano_a_entero('VL')
    with pytest.raises(RomanNumberError):
        romano_a_entero('LM')

def test_no_restas_multiplos_5():
    with pytest.raises(RomanNumberError):
        romano_a_entero('VX')
    with pytest.raises(RomanNumberError):
        romano_a_entero('LC')
    with pytest.raises(RomanNumberError):
        romano_a_entero('DM')

def test_no_repeticion_de_restas():
    with pytest.raises(RomanNumberError):
        romano_a_entero('IIX')
    with pytest.raises(RomanNumberError):
        romano_a_entero('IVIX')
    with pytest.raises(RomanNumberError):
        romano_a_entero('VIX')

def test_pa_fastidiar():
    romano_a_entero('MCMXCIX') == 1999