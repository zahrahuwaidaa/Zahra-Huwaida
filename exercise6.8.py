pet_1 = {'animal': 'dog', 'owner': 'alice'}
pet_2 = {'animal': 'cat', 'owner': 'bob'}
pet_3 = {'animal': 'rabbit', 'owner': 'charlie'}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"{pet['owner'].title()} has a {pet['animal']}.")