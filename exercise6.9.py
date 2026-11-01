favorite_places = {
    'alice': ['tokyo', 'paris'],
    'bob': ['new york'],
    'charlie': ['reykjavik', 'cairo', 'sydney'],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places:")
    for place in places:
        print(f"  - {place.title()}")