class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type.title()} cuisine.")


restaurant1 = Restaurant('sederhana', 'indonesian')
restaurant2 = Restaurant('sushi tei', 'japanese')
restaurant3 = Restaurant('pizza hut', 'italian')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()