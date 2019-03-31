from item import *
from order import Order
from menu import Menu
from inventory import Inventory
from staffSystem import StaffSystem

'''
This is the main interface for both customers and staff.
'''

class OrderSystem:

    def __init__(self, Menus: dict, Inventory: Inventory, Staff_system: StaffSystem = None):
        # order fields
        self._orders = []       # list<order>
        self._norder = 0        # total number of orders, also used as order id

        # other system fields
        self._menus = Menus     # Menus should be a dict like {"Mains": Mains, "Sides": Sides, "Drinks": Drinks}
        self._inventory = Inventory
        self._staff_system = Staff_system

    '''
    Menu part
    '''

    # get a menu
    def get_menu(self, menu_name: str) -> Menu:
        if menu_name in self._menus.keys():
            return self._menus[menu_name]
        else:
            print(f"{menu_name} menu not exist!")
    
    # get an item from its menus
    def get_item(self, item_name: str) -> Item:
        for menu in self._menus.values():
            item = menu.get_item(item_name)
            if item:
                return item
        print(f"{item_name} not in the system")

    # display a menu
    def display_menu(self, menu_name: str):
        if menu_name in self._menus.keys():
            self._menus[menu_name].display()
        else:
            print(f"{menu_name} menu not exist!")

    '''
    Order part
    '''

    # Add an order into the system
    def add_order(self, new_order: Order):
        self._orders.append(new_order)

    # return an order based on an order id
    def _get_order(self, order_id: int) -> Order:
        for order in self._orders:
            if order.order_id == order_id:
                return order
            else:
                return None

    # Make a new online order, add it into the system, and then return the order id
    def make_order(self) -> int:
        new_orderId = self._norder + 1
        new_order = Order(new_orderId)
        self._norder += 1
        self.add_order(new_order)
        return new_orderId

    # Display the details of an order
    def display_order(self, order_id: int):
        order = self._get_order(order_id)
        if order:
            order.display()

    # TODO: Add items into an order
    def add_items_in_orders(self, order_id: int, *argv: Item):
        order = self._get_order(order_id)
        for item in argv:
            if not item.is_available(self._inventory):
                print(f"{item.name} is not available!")
                return
        order.add_items(*argv)

    # TODO: Delete items from an order
    def del_items_in_orders(self, order_id: int, *argv: Item):
        order = self._get_order(order_id)
        order.delete_items(*argv)


    # TODO: Authorise payment for an order
    def pay_order(self, order_id: int):
        order = self._get_order(order_id)
        if not order:
            return
        print('Order: {}, total price: ${:.2f}'.format(order_id, order.price))

        answer = input('Authorise payment? (yes/no) ')
        if answer.lower() == 'yes':
            print('Payment authorised.')
            order.update_payment_status(True)
        else:
            print('Payment not authorised.')

    '''
    property
    '''
    @property
    def inventory(self):
        return self._inventory