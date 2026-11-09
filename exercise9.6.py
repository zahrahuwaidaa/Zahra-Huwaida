class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type.title()} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open!")


class IceCreamStand(Restaurant):
    """A specific kind of restaurant: an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'mint']

    def show_flavors(self):
        """Display the ice cream flavors available."""
        print(f"{self.restaurant_name.title()} has the following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


ice_stand = IceCreamStand('sweet corner')
ice_stand.describe_restaurant()
ice_stand.show_flavors()