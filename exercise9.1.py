class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print restaurant information."""
        print(f"Restaurant name: {self.restaurant_name.title()}")
        print(f"Cuisine type: {self.cuisine_type.title()}")

    def open_restaurant(self):
        """Print a message that the restaurant is open."""
        print(f"{self.restaurant_name.title()} is now open!")


restaurant = Restaurant('sederhana', 'indonesian')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()