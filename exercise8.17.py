def get_full_name(first_name, last_name, middle_name=''):
    """Return a neatly formatted full name."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


def greet_user(first_name, last_name):
    """Display a greeting to a user by full name."""
    full_name = get_full_name(first_name, last_name)
    print(f"Hello, {full_name}!")


def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


greet_user('jimi', 'hendrix')
describe_pet(pet_name='willie')
describe_pet('harry', 'hamster')