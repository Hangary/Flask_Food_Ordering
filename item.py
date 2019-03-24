'''
This is a class for food items such as burgers, cola and other thing.
'''


class Item(object):

    def __init__(self, name, price, type, description, ingredients, availability=True):
        self._name = name                       # string
        self._price = price                     # float
        # the type of the item: "Mains", "Sides", "Drinks"
        self._type = type
        self._description = description         # string
        self._ingredients = ingredients         # list<ingredient>
        self._availability = availability       # boolean

    # TODO: check whether this item is available in the inventory
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
        return self._ingredients[::]

    # TODO
    def __str__(self):
        return "name: {}, price: ${:.2f}, description: {}, ingredients: {}, tags: {}".format(self._name, self._price, self._description, self._ingredients, self._tags)

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
This should be a special class for the mains
'''


class Creation(Item):

    def __init__(self, name, price, type, description, ingredients, availability=True):
        super().__init__(name, price, type, description,
                         ingredients, availability=availability)

    # TODO
    def modify_ingredients(self, list_ingredients):
        self.ingredients = list_ingredients
        self._calculate_price()

    # TODO: calculate its price based on its ingredients
    def _calculate_price(self):
        pass

# i = Item('Mocha',4.50,True,'Chocolate Coffe',['Chocolate','Coffee'],"Uses Lindt White Choc")
# print(i)
