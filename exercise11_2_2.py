from exercise11_2_1 import city_country


def test_city_country():
    """Does 'Santiago, Chile' work?"""
    formatted = city_country('santiago', 'chile')
    assert formatted == 'Santiago, Chile'


def test_city_country_population():
    """Does 'Santiago, Chile - population 5000000' work?"""
    formatted = city_country('santiago', 'chile', population=5000000)
    assert formatted == 'Santiago, Chile - population 5000000'