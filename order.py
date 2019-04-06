from item import Item
from inventory import Inventory
from ingredient import Ingredient
'''
TODO: This is a class used to store information about online orders.
'''


class Order(object):

    def __init__(self, order_id: int):
        self._order_id = order_id

        # Order status fields:
        self._is_payed = False            # boolean, whether it is payed or not
        self._is_prepared = False       # boolean, whether it is prepared or not

        # Customized fields:
        # Dictionary key = item name, value = list of item (to support duplicate)
        self._items = { }
        # float, the total price for the order
        self._price = float('nan')
        # string, some special notes by the customer
        self._notes = ''

    # if Order is payed
    def update_payment_status(self, status: bool):
        self._is_payed = status

    # if Order is ready
    def update_preparation_status(self, status: bool):
        self._is_prepared = status

    # add new items into an order
    # dont call this
    def add_items(self, *argv: Item):
        for item in argv:
            if item.name in self._items:
                self._items[item.name].append(item)
            else:
                self._items[item.name] = [item]
            self.calculate_price()

    #function to delete items from order
    def delete_items(self, *argv: str):
        for item_name in argv:
            if item_name in self._items.keys():
                del self._items[item_name]
            else:
                print(f"Cannot find {item_name} in the order!")
        self.calculate_price()

    # calculate order price
    def calculate_price(self):
        price = 0
        for item_list in self._items.values():
            for item in item_list:
                price = price + item.price
        self._price = price

    # Display the items of orders
    def display(self):
        print('Order {0} has items:'.format(self._order_id))
        for item_list in self._items.values():
            for item in item_list:
                print(item)
        print('Total price: ${}'.format(self._price))
        print("Paid?",self.is_payed)
        print("Prepared?",self.is_prepared)


    
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
    def is_payed(self):
        return self._is_payed

    @property
    def order_id(self):
        return self._order_id

    @property
    def price(self):
        return self._price
    
    @is_prepared.setter
    def is_prepared(self,vara):
       self._is_prepared = vara

    '''
    str
    '''

    def __str__(self):
        return f"order id: {self._order_id}, total price: {self._price}"


if __name__ == "__main__":
    
    pass
