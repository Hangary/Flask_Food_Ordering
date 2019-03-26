from item import Item
'''
This is a class used to store menu information, which is composed of items.
'''


class Menu:

    def __init__(self, menu_name):
        self._name = menu_name   # the name for the menu, e.g. Mains, Drinks ...
        self._items = {}    # a dict for items

    # add some items into the menu
    def add_item(self, *argv):
        for item in argv:
            self._items[item.name] = item

    # get a list of items by their names
    def get_item(self, *argv):
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


if __name__ == "__main__":
    pass