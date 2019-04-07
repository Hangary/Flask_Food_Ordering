from item import *
from order import Order
from menu import Menu
from inventory import Inventory
from staffSystem import *
from system_creator import *
import csv

import pytest

@pytest.fixture(scope = "module")
def setup():
    system = create_system(
        mains=create_mains_menu("docs/Menus.csv"),
        sides=create_sides_menu("docs/Menus.csv"),
        drinks=create_drinks_menu("docs/Menus.csv"),
        inventory=create_inventory("docs/Inventory.csv"),
        staff_system=create_staffsystem("docs/StaffSystem.csv")
    )
    return system

def test_correct_login(setup):
    setup.staff_system.login('Gaurang','1234')
    assert(setup.staff_system.is_authenticated == True)

def test_incorrect_login(setup):
    setup.staff_system.logout()
    setup.staff_system.login('Gaurang','incorrect')
    assert(setup.staff_system.is_authenticated == False)

def test_updatation_order(setup):
    order_id = setup.make_order()
    setup.checkout(order_id)
    setup.update_order(order_id,'Gaurang','1234')
    assert(setup.completed_orders[0].order_id == order_id)

