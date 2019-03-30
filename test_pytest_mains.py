from OrderSystem import *
from item import *
from order import Order
from menu import Menu
from inventory import Inventory

import pytest

BURGER_BASE_PRICE = 10
WRAP_BASE_PRICE = 9
MAX_BUNS = 4
MAX_PATTIES = 3
@pytest.fixture(scope = "module")
def setup_fixture():

    sesame_bun = Ingredient(name="Sesame Bun", additional_price=1)
    muffin_bun = Ingredient(name="Muffin Bun", additional_price=1)
    basic_wrap = Ingredient(name = "Wrap", additional_price=1)
    premium_wrap = Ingredient(name = "Premium Wrap", additional_price=2)
    # patties
    chicken_patty = Ingredient(name="Chicken Patty", additional_price=2)
    vegetarian_patty = Ingredient(name="Vegetarian Patty", additional_price=2)
    # other
    tomato = Ingredient(name="tomato", additional_price=0.2)
    lettuce = Ingredient(name="lettuce", additional_price=0.2)

    '''
    Mains initializer
    '''
    # Buger
    burger = Main("Burger", BURGER_BASE_PRICE)
    burger.add_ingredients(sesame_bun, muffin_bun,
                           chicken_patty, vegetarian_patty,
                           tomato, lettuce)
    burger.set_ingredient_limit(ingredient_name="Buns", amount=MAX_BUNS)
    burger.set_ingredient_limit(ingredient_name="Patties", amount=MAX_PATTIES)
    # Wrap
    wrap = Main("Wrap", WRAP_BASE_PRICE)
    wrap.add_ingredients(basic_wrap, premium_wrap,
                         chicken_patty, vegetarian_patty,
                         tomato, lettuce)
    
    # Mains menu
    mains_menu = Menu("Mains")
    mains_menu.add_items(burger,wrap)

    # Sides menu
    LargeFries = Side("Large Fries",4)
    SmallFries = Side("Small Fries",2)
    MediumFries = Side("Medium Fries",3)
    sides_menu = Menu("Sides")
    sides_menu.add_items(SmallFries,MediumFries,LargeFries)

    # Drink menus
    coke_zero = Drink("Coke Can",2.5)
    coke_diet = Drink("Coke Bottle",4) 
    drinks_menu = Menu("Drinks")
    drinks_menu.add_items(coke_diet, coke_zero)

    # system
    menu = {
        "Mains":     mains_menu,
        "Sides":     sides_menu,
        "Drinks":    drinks_menu
    }
    system = OrderSystem(menu, None)
    return system

def test_OrderSystem_menu(setup_fixture):
    assert 'tomato' in setup_fixture.get_menu("Mains").get_item("Burger").ingredients
    #print(setup_fixture.get_menu("Mains"))
    #setup_fixture.get_menu("Mains").display()
    #assert 0


def test_items_in_menu(setup_fixture):

    assert "Burger" == setup_fixture.get_item("Burger").name
    assert "Large Fries" ==  setup_fixture.get_item("Large Fries").name
    assert "Coke Can" == setup_fixture.get_item("Coke Can").name

    ## testing prices

    assert setup_fixture.get_item("Large Fries").price == 4
    assert setup_fixture.get_item("Medium Fries").price == 3
    assert setup_fixture.get_item("Small Fries").price == 2
    assert setup_fixture.get_item("Coke Bottle").price == 4
    assert setup_fixture.get_item("SOMETHING") == None

