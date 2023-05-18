from roman_numbers import entero_a_romano

def test_uno_es_palito():
    assert entero_a_romano(1) == "I"

def test_dos_es_palito_palito():
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