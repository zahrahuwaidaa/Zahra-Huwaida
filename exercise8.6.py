def city_country(city, country):
    """Return a string formatted as 'City, Country'."""
    return f"{city.title()}, {country.title()}"

print(city_country('santiago', 'chile'))
print(city_country('tokyo', 'japan'))
print(city_country('jakarta', 'indonesia'))