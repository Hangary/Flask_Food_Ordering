from ingredient import Ingredient
'''
TODO: 
This is a class used to store inventory.
'''
### add minimum amount to sell

class Inventory(object):

    def __init__(self):
        self._ingredients = {}      # dict<Ingredient>

    # add new ingredients to the inventory
    # ingredients to be created first (aggregation relationship)
    def add_new_ingredients(self, *argv: Ingredient):
        for ingredient in argv:
            self._ingredients[ingredient.name] = ingredient

    # add or substract amount of an ingredient
    def update_stock(self, ingredient_name: str, amount: float):
        self._ingredients[ingredient_name].change(amount)
    
    def update_value(self, ingredient_name: str, amount: float):
        self._ingredients[ingredient_name].update_value(amount)

    # check an ingredient whether available (with an amount)
    def is_available(self, ingredient_name: str, amount: float =None):
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
    
    def get_ingredient(self,name):
        return self._ingredients[name]


if __name__ == "__main__":
    butter = Ingredient("butter")
    tomato = Ingredient("tomato", 10)
    inventory = Inventory()

    inventory.add_new_ingredients(butter, tomato)
    print(inventory._ingredients)
