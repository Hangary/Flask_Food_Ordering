from ingredient import Ingredient
'''
This is a class for food items such as burgers, cola and other thing.
'''


class Item(object):

    def __init__(self, name, price, type, description='N/A', availability=True):
        self._name = name                       # string
        self._price = price                     # float
        self._type = type                       # "Mains", "Sides", "Drinks"

        # optional fields:
        self._description = description         # string
        self._availability = availability       # boolean

        # other fields:
        self._ingredients = {}                  # dict<ingredient>

    # add ingredients into the item
    def add_ingredients(self, *argv):
        for ingredient in argv:
            self._ingredients[ingredient.name] = ingredient

    # TODO: check whether this item is available in the inventory, based on whether its ingredients are available
    def check_availability(self, inventory):
        pass

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def type(self):
        return self._type

    @property
    def availability(self):
        return self._availability

    @property
    def description(self):
        return self._description

    @property
    def ingredients(self):
        return self._ingredients

    def __str__(self):
        return f"name: {self._name}, price: ${self._price:.2f}, description: {self._description}, type: {self._type}"

    def __eq__(self, other):
        # assuming order of ingredient do not matter
        try:
            for attr in ['_name', '_price', '_description', '_tags']:
                if getattr(self, attr) != getattr(other, attr):
                    return False

            for attr in ['_ingredients', '_tags']:
                if set(getattr(self, attr)) != set(getattr(other, attr)):
                    return False
        except:
            return False

        return True

    def __ne__(self, other):
        return not self == other


'''
TODO:
This should be a special class for the mains.
Notes: There should be a defaulted ingredients list for a main food and corresponding limits.
'''


class Creation(Item):

    def __init__(self, name, price, type, description, ingredients, availability=True):
        super().__init__(name, price, type, description,
                         ingredients, availability=availability)
        self._max_limit = {}

    def set_ingredient_limit(self, ingredient_name, amount):
        self._max_limit[ingredient_name] = amount

    # TODO:
    def modify_ingredients(self, ingredient_name, amount):
        if self._max_limit[ingredient_name]:
            if amount < self._max_limit[ingredient_name]:
                pass
            else:
                print("more than the max amount!")
                return
        self._ingredients[ingredient_name].amount = amount
        self._calculate_price()

    # TODO: calculate its price based on its ingredients
    def _calculate_price(self):
        pass


# TODO: some unit tests here
if __name__ == "__main__":

    coke_zero = Item("Coke Zero", 2.5, "Drinks")
    print(coke_zero)
    coke_zero.add_ingredients(Ingredient("Coke Zero"), Ingredient("Ice cube"))

    for ingredient in coke_zero.ingredients:
        print(ingredient)
