from item import *
from order import Order
from menu import Menu
from inventory import Inventory

'''
This is the main interface for both customers and staff.
'''


class OrderSystem:

    def __init__(self, Menus, Inventory):
        # order fields
        self._orders = []       # list<order>
        self._norder = 0        # total number of orders, also used as order id

        # menu field
        self._menus = Menus     # Menus should be a dict like {"Mains": Mains, "Sides": Sides, "Drinks": Drinks}

        # inventory field
        self._inventory = Inventory

    '''
    Menu part
    '''

    # get a menu
    def get_menu(self, menu_name):
        if menu_name in self._menus.keys():
            return self._menus[menu_name]
        else:
            print(f"{menu_name} menu not exist!")
    
    # get an item from its menus
    def get_item(self, item_name):
        for menu in self._menus.values():
            item = menu.get_item(item_name)
            if item:
                return item
        print(f"{item_name} not in the system")

    # display a menu
    def display_menu(self, menu_name):
        if menu_name in self._menus.keys():
            self._menus[menu_name].display()
        else:
            print(f"{menu_name} menu not exist!")

    '''
    Order part
    '''

    # Add a new order
    def add_order(self, new_order):
        self._orders.append(new_order)

    # return an order based on an order id
    def _get_order(self, order_id):
        for order in self._orders:
            if order.order_id == order_id:
                return order
            else:
                return None

    # TODO: Make a new online order
    def make_order(self):
        new_order = Order(self._norder)
        self._norder += 1

        flag_finished = [False, False, False]

        while flag_finished[0] == False:
            print(self.display_mains_menu())
            # an input, which choose an item
            user_input = ...
            if user_input.isdigit():
                pass
                item = Item(...)
                new_order.add_item("Mains", item)
            elif user_input == 'f':
                flag_finished[0] = True
            else:
                print("Please reinput")

        while flag_finished[1] == False:
            print(self.display_sides_menu())
            # an input, which choose an item
            user_input = ...
            if user_input.isdigit():
                pass
                item = Item(...)
                new_order.add_item("Sides", item)
            elif user_input == 'f':
                flag_finished[1] = True
            else:
                print("Please reinput")

        while flag_finished[1] == False:
            print(self.display_drinks_menu())
            # an input, which choose an item
            user_input = ...
            if user_input.isdigit():
                pass
                items = chosen_item
                new_order.add_item("Drinks", item)
            elif user_input == 'f':
                flag_finished[1] = True
            else:
                print("Please reinput")

        # TODO: display order price and items

        # add this order into the system
        self.add_order(new_order)

    # TODO: Display the details of an order

    def display_order(self, order_id):
        order = self._get_order(order_id)
        if order:
            order.display()

    # TODO: Authorise payment for an order
    def pay_order(self, order_id):
        order = self._get_order(order_id)
        if not order:
            return
        print('Table: {}, total: ${:.2f}'.format(table_number, total))

        answer = input('Authorise payment? (yes/no) ')
        if answer.lower() == 'yes':
            print('Payment authorised.')
            self._order_logs.append(table)
        else:
            print('Payment not authorised.')