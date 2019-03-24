from item import Item
'''
This is a class used to store information about online orders.
'''


class Order(object):

    def __init__(self, order_id):
        self._order_id = order_id      # int, given by the system
        self._is_payed = False         # boolean, whether it is payed or not
        self._is_prepared = False         # boolean, whether it is prepared or not
        # dict{item}, contain 3 lists used to contain the food items chosen by the customer
        self._items = {"Mains": [], "Sides": [], "Drinks": []}
        self._notes = ""            # string, some special notes by the customer
        self._price = 0             # int, the total price for the order

    # Order is payed
    def update_payment_status(self):
        self._is_payed = True

    # Order is ready
    def update_preparation_status(self):
        self._is_prepared = True

    # add new items into order
    # item_type should be "Mains", "Sides" and "Drinks"
    def add_item(self, item_type, item):
        self._items[item_type].append(item)

    # calculate order price
    def calculate_order_price(self):
        price = 0
        for item_type in self._items:
            for item in item_type:
                price = price + item.price
        self._price = price

    # @property
    # def item(self):
    #     return self._items

    # @item.setter
    # def item(self, new_item):
    #     self._price = new_item

    @property
    def is_prepared(self):
        return self._is_prepared

    @property
    def order_id(self):
        return self._order_id

    # def __str__(self):
    #     return str(self._items) + "Special Notes: " + self._notes

    # Display the list of orders that this table currentlyhas
    def display(self):
        print('Order {0} has items:'.format(self._order_id))
        for item_type in self._items:
            for item in item_type:
                print(item)

# i = Item('Mocha',4.50,True,'Chocolate Coffe',['Chocolate','Coffee'],"Uses Lindt White Choc")
# o = Order(0,i,"2 sugar")
# print("{}:{}".format(o,o.get_order_price()))
