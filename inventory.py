from item import Item

class Inventory(object):

    def __init__(self):
        self._ingredients = {}      # dict<Ingredient>

    def add_new_ingredient(self, ingredient):
        self.