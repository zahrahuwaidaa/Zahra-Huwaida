class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type.title()} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open!")

    def set_number_served(self, number):
        """Set the number of customers served."""
        self.number_served = number

    def increment_number_served(self, number):
        """Increment the number of customers served."""
        self.number_served += number


restaurant = Restaurant('sederhana', 'indonesian')

print(f"Customers served: {restaurant.number_served}")

restaurant.number_served = 10
print(f"Customers served: {restaurant.number_served}")

restaurant.set_number_served(50)
print(f"Customers served: {restaurant.number_served}")

restaurant.increment_number_served(25)
print(f"Customers served: {restaurant.number_served}")