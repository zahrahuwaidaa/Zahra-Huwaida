class User:
    """A class to model a user profile."""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"User: {self.first_name.title()} {self.last_name.title()}")


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = [
            'can add post',
            'can delete post',
            'can ban user',
        ]

    def show_privileges(self):
        """Show the admin's privileges."""
        print(f"{self.first_name.title()} has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin = Admin('budi', 'santoso')
admin.describe_user()
admin.show_privileges()