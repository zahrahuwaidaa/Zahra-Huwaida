def city_country(city, country, population=None):
    """Return a string formatted as 'City, Country'."""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    return f"{city.title()}, {country.title()}"