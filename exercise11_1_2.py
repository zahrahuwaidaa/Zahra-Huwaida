from exercise11_1_1 import city_country


def test_city_country():
    """Does 'Santiago, Chile' work?"""
    formatted = city_country('santiago', 'chile')
    assert formatted == 'Santiago, Chile'