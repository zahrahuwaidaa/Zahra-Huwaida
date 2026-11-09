from pathlib import Path
import json


def get_stored_user_info(path):
    """Get stored user info if available."""
    if path.exists():
        contents = path.read_text()
        return json.loads(contents)
    return None


def get_new_user_info(path):
    """Prompt for new user information."""
    username = input("What is your username? ")
    age = input("How old are you? ")
    city = input("What city do you live in? ")
    user_info = {'username': username, 'age': age, 'city': city}
    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info


def greet_user():
    """Greet the user by name."""
    path = Path('user_info.json')
    user_info = get_stored_user_info(path)

    if user_info:
        correct = input(
            f"Is '{user_info['username']}' the correct username? (yes/no): "
        )
        if correct == 'yes':
            print(f"Welcome back, {user_info['username']}!")
            return

    user_info = get_new_user_info(path)
    print(f"We'll remember you when you come back, {user_info['username']}!")


greet_user()