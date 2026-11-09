from pathlib import Path
import json

path = Path('user_info.json')

if path.exists():
    contents = path.read_text()
    user_info = json.loads(contents)
    print("Here's what I remember about you:")
    for key, value in user_info.items():
        print(f"{key.title()}: {value}")
else:
    username = input("What is your username? ")
    age = input("How old are you? ")
    city = input("What city do you live in? ")

    user_info = {'username': username, 'age': age, 'city': city}
    contents = json.dumps(user_info)
    path.write_text(contents)
    print("Thanks! I'll remember that.")