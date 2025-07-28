class Ingredient:
    def __init__(self, name, unit):
        self.name = name
        self.unit = unit


class Recipe:
    def __init__(self):
        self.ingredients = {}
        self.method =''

    def add_ingredient(self, ingredient, amount):

        if ingredient in self.ingredients:
            print("Ingredient already added")
        else:
            self.ingredients[ingredient] = amount

    def add_method(self):
        self.method = input("Please enter the method here: ")

    def print_ingredients(self):
        for key, value in self.ingredients.items():
                    print(key.name + ": " + str(value) + key.unit)
