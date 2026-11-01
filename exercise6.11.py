cities = {
    'tokyo': {
        'country': 'japan',
        'population': 14_000_000,
        'fact': 'Tokyo is the most populous metropolitan area in the world.',
    },
    'paris': {
        'country': 'france',
        'population': 2_100_000,
        'fact': 'Paris has the Eiffel Tower.',
    },
    'cairo': {
        'country': 'egypt',
        'population': 9_500_000,
        'fact': 'Cairo is near the ancient pyramids of Giza.',
    },
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"  Country: {info['country'].title()}")
    print(f"  Population: {info['population']:,}")
    print(f"  Fact: {info['fact']}")