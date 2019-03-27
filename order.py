from item import Item
from ingredient import Ingredient
'''
TODO: This is a class used to store information about online orders.
'''


class Order(object):

    def __init__(self, order_id):
        self._order_id = order_id

        # Order status fields:
        self._is_payed = False            # boolean, whether it is payed or not
        self._is_prepared = False         # boolean, whether it is prepared or not

        # Customized fields:
        # 3 lists used to contain the food items chosen by the customer
        self._items = {"Mains": [], "Sides": [], "Drinks": []}
        # float, the total price for the order
        self._price = float('nan')
        # string, some special notes by the customer
        self._notes = ''

    # if Order is payed
    def update_payment_status(self):
        self._is_payed = True

    # if Order is ready
    def update_preparation_status(self):
        self._is_prepared = True

    # add new items into order, item_type should be "Mains", "Sides" and "Drinks"
    def add_items(self, *argv):
        for item in argv:
            if item.type in ("Mains", "Sides", "Drinks"):
                self._items[item.type].append(item)
            else:
                print("Wrong input!")
        self.calculate_price()

    # calculate order price
    def calculate_price(self):
        price = 0
        for items in self._items.values():
            for item in items:
                price = price + item.price
        self._price = price

    # Display the items of orders
    def display_items(self):
        print('Order {0} has items:'.format(self._order_id))
        for item_type in self._items.values():
            for item in item_type:
                print(item)

    '''
    Property
    '''

    @property
    def items(self):
        return self._items

    @property
    def is_prepared(self):
        return self._is_prepared

    @property
    def order_id(self):
        return self._order_id

    '''
    str
    '''

    def __str__(self):
        return f"order id: {self._order_id}, total price: {self._price}"


if __name__ == "__main__":

    fries_l = Item("Fries - Large", 5, "Sides")

    coke_zero_m = Item("Coke Zero - Medium", 2.5, "Drinks")
    coke_zero_m.add_ingredients(Ingredient(
        "Coke Zero"), Ingredient("Ice cube"))

    new_order = Order(45)
    new_order.add_items(fries_l, coke_zero_m)
    new_order.calculate_price()
    print(new_order)
    new_order.display_items()
