class Employee:
    """A class to model an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Give the employee a raise (default $5,000)."""
        self.annual_salary += amount