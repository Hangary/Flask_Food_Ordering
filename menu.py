from item import Item
'''
This is a class used to store menu information, which is composed of items.
'''
class Menu:

    def __init__(self, name):
        self._name = name   # the name for the menu, e.g. Mains, Drinks ...
        self._items = {}    # a dict for items

    # add new item into the menu
    def add_item(self, name, price, availability, description, ingredients, tags):
        self._items[name] = Item(name, price, availability, description, ingredients, tags)

    # get all the details of the items inside the menu
    def display(self):
        return self._items.values()

    # print all the values inside the menu
    def print_menu(self):
        for item in self._items.keys():
            print(self.get_item(item))
    
    # get the detail for an item by its name
    def get_item(self, name):
        # if name in self._items.keys():
        #     print("menu-item present")
        return self._items[name]

    # get all the items inside the menu
    def get_items(self):
        return self._items