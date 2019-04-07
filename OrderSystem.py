from item import *
from order import Order
from menu import Menu
from inventory import Inventory
from staffSystem import *
from copy import deepcopy
import math
'''
This is the main interface for both customers and staff.
'''
import pytest

class OrderSystem:

    def __init__(self, Menus: dict, Inventory: Inventory, Staff_system = "NONE"):
        # order fields
        self._pending_orders = []       # list<order>
        self._completed_orders = []     #list<order>
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
        return f"{item_name} not in the system"

    # display a menu
    def display_menu(self, menu_name: str):
        if menu_name in self._menus.keys():
            self._menus[menu_name].display()
        else:
            print(f"{menu_name} menu not exist!")
            return f"{menu_name} menu not exist!"

    '''
    Order part
    '''

    # Add an order into the system
    def _add_order(self, new_order: Order):
        self._pending_orders.append(new_order)

    # return an order based on an order id from pending order
    def _get_pendingorder(self, order_id: int) -> Order:
        for order in self._pending_orders:
            if order.order_id == order_id:
                return order
        else:
            return None
    
    # return an order based on an order id from pending order
    def _get_completedorder(self, order_id: int) -> Order:
        for order in self._completed_orders:
            if order.order_id == order_id:
                return order
        else:
            return None

    # Make a new online order, add it into the system, and then return the order id
    def make_order(self) -> int:
        new_orderId = self._norder + 1
        new_order = Order(new_orderId)
        self._norder += 1
        self._add_order(new_order)
        return new_orderId

    # Display the details of an order
    # Use this function to display order at anytime
    def display_order(self, order_id: int):
        order = self._get_pendingorder(order_id)
        if order == None:
            for order in self._completed_orders:
                if order.order_id == order_id:
                    break
        if order:
            order.display()

    # TODO: Add items into an order
    def add_items_in_orders(self, order_id: int, *argv: Item):
        order = self._get_pendingorder(order_id)
        for item in argv:
            if not item.is_available(self._inventory):
                print(f"{item.name} is not available!")
            else:
                item = deepcopy(item)
                order.add_items(item)
        #order.add_items(*argv)

    # TODO: Delete items from an order
    def del_items_in_orders(self, order_id: int, *argv: str):
        order = self._get_pendingorder(order_id)
        order.delete_items(*argv)


    # TODO: Authorise payment for an order
    def _pay_order(self, order: Order):
        print('Order: {}, total price: ${:.2f}'.format(order.order_id, order.price))

        answer = 'yes' #input('Authorise payment? (yes/no) ')
        if answer.lower() == 'yes':
            print('Payment authorised.')
            order.update_payment_status(True)
        else:
            print('Payment not authorised.')
    # function for staff to remove orders which are completed from the list
    def update_order(self,order_id,username = 'NONE',password = 'NONE'):
        #authorising to make sure only staff can remove orders
        if self._staff_system.is_authenticated == False:
            if self._staff_system.login(username,password) == False:
                print('Invalid login')
                return
        order = self._get_pendingorder(order_id)
        if(order and order in self._pending_orders):
            if(order.is_payed == True):
                order.is_prepared  = True
                self._pending_orders.remove(order)
                self._completed_orders.append(order)
            else:
                print("Payment for the order not completed")
        else:
            print("Order already completed")

    def display_order_lists(self):
        print("-----List of Pending orders---------")
        for orders in self._pending_orders:
            print(orders)
        print("-----List of completed orders---------")
        for complete_orders in self._completed_orders:
            print(complete_orders)
    #checking out after placing order
    def checkout(self,order_id: int):
        order = self._get_pendingorder(order_id)
        if not order:
            print("Order does not exist")
            return
        print("Your final order is")
        self.display_order(order_id)
        new_inventory = deepcopy(self._inventory)
        for items_list in order.items.values():
            for item in items_list:
                for ingredient_list in item.ingredients.values():
                    if ingredient_list.__class__.__name__ == "Ingredient":
                        new_inventory.update_stock(ingredient_list.name,-ingredient_list.amount)
                        if (new_inventory.is_available(ingredient_list.name,1) == True):
                            unavailable_order = 0 
                        else:
                            unavailable_order = 1
                            break
                    else: 
                        for ingredient in ingredient_list.values():
                            assert(ingredient.__class__.__name__ == "Ingredient")
                            if not isNaN(ingredient.amount):
                                new_inventory.update_stock(ingredient.name,-ingredient.amount)
                                if (new_inventory.is_available(ingredient.name,1) == True):
                                    unavailable_order = 0 
                                else:
                                    unavailable_order = 1
                                    break
                    
        if unavailable_order == 0:
            self._pay_order(order)
        #updating inventory after order is paid
            if (order.is_payed):
                for items_list in order.items.values():
                    for item in items_list:
                        for ingredient_list in item.ingredients.values():
                            if ingredient_list.__class__.__name__ == "Ingredient":
                                self._inventory.update_stock(ingredient_list.name,-ingredient_list.amount)
                            else: 
                                for ingredient in ingredient_list.values():
                                    assert(ingredient.__class__.__name__ == "Ingredient")
                                    if not isNaN(ingredient.amount):
                                        self._inventory.update_stock(ingredient.name,-ingredient.amount)
            else:
                self._pending_orders.remove(order)
        else:
            print("Order unavailable due to shortage of ingredients")
            self._pending_orders.remove(order)


    '''
    property
    '''
    @property
    def inventory(self):
        return self._inventory
    
    @property
    def pending_orders(self):
        return self._pending_orders
    
    @property
    def completed_orders(self):
        return self._completed_orders

    @property
    def total_order(self):
        return self._norder
    
    @property
    def staff_system(self):
        return self._staff_system

