favorite_numbers = {
    'alice': [7, 21],
    'bob': [13, 42, 100],
    'charlie': [3],
    'diana': [5, 10],
    'eric': [21],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers:")
    for number in numbers:
        print(f"  - {number}")