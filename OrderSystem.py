from item import Item
from order import Order
from menu import Menu
from inventory import Inventory

class OrderSystem:

    def __init__(self):
        self._orders = []                   # list<order>
        self._norder = 0                    # total number of orders, also used as order id
        self._mains_menu = Menu("Mains")    # Main menu
        self._sides_menu = Menu("Sides")    # Sides menu
        self._drinks_menu = Menu("Drinks")  # Drinks menu
        # self._inventory = Inventory()
        # self._admin_system = admin_system

    #def get_menu_items(self):
    #    return self._menu.get_items()

    # Display menu
    def display_mains_menu(self):
        # return self._menu.display()
        return self._mains_menu
    
    def display_sides_menu(self):
        # return self._menu.display()
        return self._sides_menu
    
    def display_drinks_menu(self):
        # return self._menu.display()
        return self._drinks_menu
    
    # TODO
    def display_item(self, name):
        if name == "":
            return "Item name is empty"
        if not self._menu.get_item(name):
            return "Item doesn't exist"
        return self._menu.get_item(name)

    # Add a new order
    def add_order(self, new_order):
        self._orders.append(new_order)

    # TODO
    # Make a new online order
    def make_order(self):
        new_order = Order(self._norder)
        self._norder += 1
        
        flag_finished  = [False, False, False]

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
                item = Item(...)
                new_order.add_item("Drinks", item)
            elif user_input == 'f':
                flag_finished[1] = True
            else:
                print("Please reinput")
        
        # TODO: display order price and items

        # add this order into the system
        self.add_order(new_order)


    # TODO: Display the details of an order
    def display_table(self, order_id):
        order = self.get_order(order_id)
        if order:
            order.display()

    # return an order based on an order id
    def get_order(self, order_id):
        for order in self._orders:
            if order.order_id == order_id:
                return order
            else:
                return None


    # TODO: Authorise payment for an order
    def pay_for_table(self, table_number):
        table = self._get_table(table_number)
        print(table.order_name + ":" + table._table_number)
        if not table:
            return
        
        total = self._finalise_total(table)
        print('Table: {}, total: ${:.2f}'.format(table_number, total))

        answer = input('Authorise payment? (yes/no) ')
        if answer.lower() == 'yes':
            print('Payment authorised.')
            self._order_logs.append(table)
        else:
            print('Payment not authorised.')


