person_1 = {'first': 'albert', 'last': 'einstein', 'age': 76, 'city': 'princeton'}
person_2 = {'first': 'marie', 'last': 'curie', 'age': 66, 'city': 'paris'}
person_3 = {'first': 'isaac', 'last': 'newton', 'age': 84, 'city': 'london'}

people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first'].title()} {person['last'].title()}"
    print(f"\nName: {full_name}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].title()}")