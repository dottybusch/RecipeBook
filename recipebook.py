class Ingredient:
    def __init__(self, name, unit):
        self.name = name
        self.unit = unit


class Recipe:
    def __init__(self,name):
        self.ingredients = {}
        self.method =''
        self.name = name
      

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

    def write_recipe(self, file):
        items = []
        for key, value in Cake.ingredients.items():
            items.append(key.name + ": " + str(value) + key.unit)
        file = open(file, mode = "a+")
        file.write("\n")
        file.write("--- " + self.name.upper() + " ---")
        file.write("\n\nINGREDIENTS\n__________________\n")
        for item in items:
            file.write(item)
            file.write("\n")
        file.write("\n\nMETHOD\n__________________\n")
        file.write(self.method)
        file.write("\n\n\n")
        file.close()

Sugar = Ingredient("Sugar", "g")
Flour = Ingredient("Flour", "g")
Eggs = Ingredient("Eggs", "")
Milk = Ingredient("Milk", "ml")

