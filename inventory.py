from ingredient import Ingredient
'''
TODO: 
This is a class used to store inventory.
'''


class Inventory(object):

    def __init__(self):
        self._ingredients = {}      # dict<Ingredient>

    # add new ingredients to the inventory
    # ingredients to be created first (aggregation relationship)
    def add_new_ingredients(self, *argv):
        for ingredient in argv:
            self._ingredients[ingredient.name] = ingredient

    # add or substract amount of an ingredient
    def update_stock(self, ingredient_name, amount):
        self._ingredients[ingredient_name].change(amount)

    # check an ingredient whether available (with an amount)
    def is_available(self, ingredient_name, amount=False):
        if amount or (amount == 0):
            return (self._ingredients[ingredient_name].amount >= amount)
        else:
            return self._ingredients[ingredient_name].is_soldout

    # display all the unavailable ingredients in the inventory
    def display_unavailable_ingredients(self):
        unavailable_ingredients = []
        for ingredient in self._ingredients:
            if ingredient.is_soldout:
                unavailable_ingredients.append(ingredient.name)
        return unavailable_ingredients


if __name__ == "__main__":
    butter = Ingredient("butter")
    tomato = Ingredient("tomato", 10)
    inventory = Inventory()

    inventory.add_new_ingredient(butter, tomato)
    print(inventory._ingredients)
