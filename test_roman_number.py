from roman_numbers import entero_a_romano, RomanNumberError
import pytest

def test_uno_es_palito():
    assert entero_a_romano(1) == "I"

def test_dos_es_palito_dos_veces():
    assert entero_a_romano(2) == "II"

def test_tres_es_palito_tres_veces():
    assert entero_a_romano(3) == "III"

def test_cuatro_es_palito_uve():
    assert entero_a_romano(4) == "IV"

def test_cinco_es_uve():
    assert entero_a_romano(5) == "V"

def test_seis_es_uve_palito():
    assert entero_a_romano(6) == "VI"

def test_siete_es_uve_y_dos_palitos():
    assert entero_a_romano(7) == "VII"

def test_ocho_es_uve_y_tres_palitos():
    assert entero_a_romano(8) == "VIII"

def test_nueve_es_palito_y_equis():
    assert entero_a_romano(9) == "IX"

def test_diez_es_equis():
    assert entero_a_romano(10) == "X"

def test_veinte_es_dos_equis():
    assert entero_a_romano(20) == "XX"

def test_resto_decenas():
    assert entero_a_romano(30) == "XXX"
    assert entero_a_romano(40) == "XL"
    assert entero_a_romano(50) == "L"
    assert entero_a_romano(60) == "LX"
    assert entero_a_romano(70) == "LXX"
    assert entero_a_romano(80) == "LXXX"
    assert entero_a_romano(90) == "XC"

def test_once_es_equis_palito():
    assert entero_a_romano(11) == "XI"

def test_101_es_C_palito():
    assert entero_a_romano(101) == "CI"

def test_numeros_raros():
    assert entero_a_romano(2345) == "MMCCCXLV"
    assert entero_a_romano(3999) == "MMMCMXCIX"

def test_cero_es_nada():
    assert entero_a_romano(0) == ""

def test_4000_es_error():
    with pytest.raises(RomanNumberError):
        entero_a_romano(4000)