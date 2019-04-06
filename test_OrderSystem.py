from item import *
from order import Order
from menu import Menu
from inventory import Inventory
from staffSystem import *
from system_creator import *
import csv

import pytest

@pytest.fixture
def setup():
    system = create_system(
        mains=create_mains_menu("docs/Menus.csv"),
        sides=create_sides_menu("docs/Menus.csv"),
        drinks=create_drinks_menu("docs/Menus.csv"),
        inventory=create_inventory("docs/Inventory.csv"),
        staff_system=create_staffsystem("docs/StaffSystem.csv")
    )
    return system

def test_wrong_menu(setup):
    assert("Wrong name menu not exist!" == setup.display_menu("Wrong name"))

def test_wrong_item(setup):
    assert("Wrong item not in the system" == setup.get_item("Wrong item"))

def test_correct_item(setup):
    with open("docs/Menus.csv") as f:
        nameList = []
        reader = csv.DictReader(f)
        for row in reader:
            nameList.append(row["Item Name"])
    for name in nameList:
        assert(name == setup.get_item(name).name)

def test_make_order(setup):
    assert setup.total_order == 0
    setup.make_order()
    assert setup.total_order == 1


