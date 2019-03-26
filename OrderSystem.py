from item import Item
from order import Order
from menu import Menu
from inventory import Inventory


class OrderSystem:

    def __init__(self):
        # order fields
        self._orders = []                   # list<order>
        self._norder = 0                    # total number of orders, also used as order id

        # menu field
        # TODO right now it is composition but should be aggregation 
        self._menus = {"Mains":   Menu("Mains"),
                      "Sides":    Menu("Sides"),
                      "Drinks":   Menu("Drinks")}

        # inventory field
        self._inventory = Inventory()

        # admin field
        # self._admin_system = admin_system

    # def get_menu_items(self):
    #    return self._menu.get_items()

    '''
    menu part
    '''

    # Display a menu
    def display_menu(self, menu_name):
        # return self._menu.display()
        if menu_name == "Mains":
            return self._menus["Mains"]
        elif menu_name == "Sides":
            return self._menus["Sides"]
        elif menu_name == "Drinks":
            return self._menus["Drinks"]
        else:
            return None

    # TODO
    def display_item(self, name):
        if name == "":
            return "Item name is empty"
        if not self._menus[""].get_item(name):
            return "Item doesn't exist"
        return self._menus[""].get_item(name)

    '''
    order part
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
