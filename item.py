from ingredient import *
'''
This is a class for food items such as burgers, drinks, sides
A completely customized burger with many ingredients will be classified as an item
to be put in an order

An item that has every ingredients for a particular type (main,side,drinks) will be used
to show in menu.

User should see the lists of available ingredients in the item through menu through system.
And through the system, user may create their item using shown ingredients and add to their order
'''


class Item(object):

    def __init__(self, name, price, type, description='N/A', availability=True):
        self._name = name                       # string
        self._price = price                # float
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

    '''
    Property
    '''

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

    '''
    str, equal, notequal
    '''

    def __str__(self):
        return (f"{self._type}: {self._name}, price: ${self._price:.2f}, description: {self._description}")

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
# when we instantiate main object (FOR MENU) price should be start at 0
'''
From the specs I think we might need to give single, double, triple burger options to customer
'''


class Main(Item):

    def __init__(self, name, price=0, description='N/A', availability=True):
        super().__init__(name, price, "Mains", description, availability)
        # dict<Ingredient>
        self._ingredients = {
            'Bun':      {},
            'Patty':   {},
            'Other':    {}  # and other ingredients
        }
        # dict<int>
        self._max_limit = {
            'Bun':      False,
            'Patty':   False
            # and other ingredients
        }
        # float, price + additional price
        self._total_price = price
    
    def add_ingredients(self, *argv):
        for ingredient in argv:
            if 'Bun' in ingredient.name:
                self._ingredients['Bun'][ingredient.name] = ingredient
            elif 'Patty' in ingredient.name:
                self._ingredients['Patty'][ingredient.name] = ingredient
            else:
                self._ingredients['Other'][ingredient.name] = ingredient
    
    def set_ingredient_limit(self, ingredient_name, amount):
        if ingredient_name != 'Bun' and ingredient_name != 'Patty' and ingredient_name not in self._ingredients['Others'].values():
            print(f"<{ingredient_name}> not in the item!")
            return f"<{ingredient_name}> not in the item!"
        self._max_limit[ingredient_name] = amount

    def modify_buns(self, *argv):
        # check whether larger than the max limit
        total_amount = 0
        for ingredient in argv:
            total_amount += ingredient.amount
        if total_amount > self._max_limit['Bun']:
            print("Buns are more than the max amount!")
            return "Buns are more than the max amount!"
        # add ingredients into dict
        for ingredient in argv:
            self._ingredients['Bun'][ingredient.name] = ingredient
        self.calculate_price()

    def modify_patties(self, *argv):
        # check whether larger than the max limit
        total_amount = 0
        for ingredient in argv:
            total_amount += ingredient.amount
        if total_amount > self._max_limit['Patty']:
            print("Patties are more than the max amount!")
            return "Patties are more than the max amount!"
        # add ingredients into dict
        for ingredient in argv:
            self._ingredients['Patty'][ingredient.name] = ingredient
        self.calculate_price()

    def modify_other_ingredients(self, *argv):
        for ingredient in argv:
            if ingredient.name in self._max_limit.keys() and ingredient.amount > self._max_limit[ingredient.name]:
                print(f"<{ingredient.name}> more than the max amount!")
                return f"<{ingredient.name}> more than the max amount!"
            self._ingredients['Other'][ingredient.name] = ingredient
        self.calculate_price()

    def calculate_price(self):
        total_price = self._price
        for ingredient_type in self._ingredients.values(): 
            for ingredient in ingredient_type.values():
                if not isNaN(ingredient.amount) and not isNaN(ingredient.additional_price):
                    total_price += ingredient.additional_price * ingredient.amount
        self._total_price = total_price

    def __str__(self):
        Buns = [f"{bun.name}: {bun.amount}" for bun in self._ingredients['Bun'].values() if not isNaN(bun.amount) and bun.amount > 0]
        Patties = [f"{patty.name}: {patty.amount}" for patty in self._ingredients['Patty'].values() if not isNaN(patty.amount) and patty.amount > 0]
        Others = [f"{other.name}: {other.amount}" for other in self._ingredients['Other'].values() if not isNaN(other.amount) and other.amount > 0]

        return (f"{self._type}: {self._name}, \ningredient: \nBuns: {Buns} \nPatties: {Patties} \nOthers: {Others} \nprice: ${self._total_price:.2f}, \ndescription: {self._description}")


class Side(Item):

    def __init__(self, name, price, description='N/A', availability=True):
        super().__init__(name, price, "Sides", description, availability)


class Drink(Item):

    def __init__(self, name, price, description='N/A', availability=True):
        super().__init__(name, price, "Drinks", description, availability)


# TODO: some unit tests here
if __name__ == "__main__":

    coke_zero = Drink("Coke Zero", 2.5)
    print(coke_zero)
    coke_zero.add_ingredients(Ingredient("Coke Zero"), Ingredient("Ice cube"))

    for ingredient in coke_zero.ingredients:
        print(ingredient)
