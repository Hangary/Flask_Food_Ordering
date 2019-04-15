from src.item import *
from src.order import Order
from src.menu import Menu
from src.inventory import Inventory
from src.staff_system import *
from src.system_creator import *
import csv
import pytest

@pytest.fixture()
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
    setup.staff_system.login('Gaurang','12355')
    assert(setup.staff_system.is_authenticated == False)

def test_updatation_order_correctlogin(setup):
    order_id = setup.make_order()
    someList = ["Coke Can","Nugget 6 pack","OrangeJuice_Small","Med Fries"]
    setup.add_items_in_orders(
        order_id,
        setup.get_item(someList[0]),
        setup.get_item(someList[1]),
        setup.get_item(someList[2]),
        setup.get_item(someList[3])
    )
    setup.checkout(order_id)
    setup.update_order(order_id,'Gaurang','1234')
    assert(setup.completed_orders[0].order_id == order_id)

def test_updatation_order_incorrectlogin(setup):
    setup.staff_system.logout()
    order_id = setup.make_order()
    someList = ["Coke Can","Nugget 6 pack","OrangeJuice_Small","Med Fries"]
    setup.add_items_in_orders(
        order_id,
        setup.get_item(someList[0]),
        setup.get_item(someList[1]),
        setup.get_item(someList[2]),
        setup.get_item(someList[3])
    )
    setup.checkout(order_id)
    flag = len(setup.completed_orders)
    setup.staff_system.logout()
    setup.update_order(order_id,'Gaurang','12355')
    assert((len(setup.completed_orders) == flag))
    assert(setup.staff_system.is_authenticated == False)

def test_updation_order_invalid_order(setup):
    order_id = 464785
    flag = len(setup.completed_orders)
    setup.staff_system.logout()
    setup.update_order(order_id,'Gaurang','1234')
    assert((len(setup.completed_orders) == flag))

def test_updationof_complete_order(setup):
    order_id = setup.make_order()
    someList = ["Coke Can","Nugget 6 pack","OrangeJuice_Small","Med Fries"]
    setup.add_items_in_orders(
        order_id,
        setup.get_item(someList[0]),
        setup.get_item(someList[1]),
        setup.get_item(someList[2]),
        setup.get_item(someList[3])
    )
    setup.update_order(order_id,'Gaurang','1234')
    flag = len(setup.completed_orders)
    setup.update_order(order_id,'Gaurang','1234')
    assert((len(setup.completed_orders) == flag))