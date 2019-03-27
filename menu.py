from item import *
'''
Finished:
This is a class used to store menu information, which is composed of items.
'''


class Menu:

    def __init__(self, menu_name):
        # the name for the menu, e.g. Mains, Drinks ...
        self._name = menu_name
        self._nitems = 0         # the number of items inside
        self._items = {}    # a dict for items

    # add some items into the menu
    def add_items(self, *argv):
        for item in argv:
            self._items[item.name] = item
            self._nitems += 1

    # get a list of items by their names
    def get_items(self, *argv):
        items = []
        for item_name in argv:
            if item_name in self._items.keys():
                items.append(self._items[item_name])
        return items

    # print all the items inside the menu
    def display(self):
        for item in self._items.values():
            print(item)

    # put items into an order
    def putin_order(self, order, *argv):
        for item_name in argv:
            item = self.get_item(item_name)
            if item:
                order.add_item(item)

    '''
    Property
    '''

    @property
    def name(self):
        return self._name

    @property
    def nitem(self):
        return self._nitems

    '''
    str
    '''

    def __str__(self):
        return f"Menu {self._name}: {self._nitems} item(s)"


if __name__ == "__main__":
    coke_zero = Drink("Coke Zero", 2.5)
    coke_diet = Drink("Coke Diet", 2.5) 
    drink_menu = Menu("Drink")
    drink_menu.add_items(coke_diet, coke_zero)
    print(drink_menu)
    drink_menu.display()