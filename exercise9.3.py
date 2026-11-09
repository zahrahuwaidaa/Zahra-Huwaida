class User:
    """A class to model a user profile."""

    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"User: {self.first_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"City: {self.city.title()}")

    def greet_user(self):
        """Print a personalized greeting."""
        print(f"Hello, {self.first_name.title()}! Welcome back.")


user1 = User('budi', 'santoso', 25, 'jakarta')
user2 = User('siti', 'rahma', 30, 'bandung')

user1.describe_user()
user1.greet_user()
print()
user2.describe_user()
user2.greet_user()