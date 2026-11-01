favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

people = ['jen', 'sarah', 'michael', 'phil', 'anna']

for person in people:
    if person in favorite_languages:
        print(f"{person.title()}, thank you for taking the poll!")
    else:
        print(f"{person.title()}, please take our poll!")