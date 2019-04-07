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

def test_add_order(setup):
    # add some drinks and sides
    # continue from above
    assert setup.total_order == 1
    someList = ["Coke Can","Nugget 6 pack","OrangeJuice_Small","Med Fries"]
    setup.add_items_in_orders(
        1,
        setup.get_item(someList[0]),
        setup.get_item(someList[1]),
        setup.get_item(someList[2]),
        setup.get_item(someList[3])
    )
    for itemName in someList:
        assert(itemName in setup._get_order(1).items.keys())

def test_remove_order(setup):
    
    assert setup.total_order == 1
    someList = ["Coke Can","Nugget 6 pack","OrangeJuice_Small"]
    setup.del_items_in_orders(1,someList[0],someList[1],someList[2])
    for itemName in someList:
        assert(itemName not in setup._get_order(1).items.keys())
    assert("Med Fries" in setup._get_order(1).items.keys())

def test_add_mains_to_order(setup):

    assert setup.total_order == 1
    setup.add_items_in_orders(1,setup.get_item("Burger"),setup.get_item("Wrap"))
    assert "Burger" in setup._get_order(1).items.keys()
    assert "Wrap" in setup._get_order(1).items.keys()
    
def test_modify_mains(setup):

    #Creating Ingredients
    sesame_bun = Ingredient(name="Sesame Bun", amount=1, additional_price=1)
    muffin_bun = Ingredient(name="Muffin Bun", amount=1, additional_price=1)
    wrap = Ingredient(name = "Wrap", amount= 2, additional_price=1)
    # patties
    chicken_patty = Ingredient(name="Chicken Patty", amount=1, additional_price=2)
    vegetarian_patty = Ingredient(name="Vegetarian Patty",amount=1, additional_price=2)
    beef_patty = Ingredient(name="Beef Patty",amount=1,additional_price=2)
    # other
    tomato = Ingredient(name="Tomato", amount=1, additional_price=0.2)
    lettuce = Ingredient(name="Lettuce", amount=1, additional_price=0.2)
    cheddar_cheese = Ingredient(name = "Cheddar Cheese", amount=1, additional_price= 0.5)
    swiss_cheese = Ingredient(name = "Swiss Cheese", amount = 1, additional_price= 0.5)
    sauce = Ingredient(name = "Tomato Sauce", amount= 1, additional_price=0.1)

    IngListBurger = [sesame_bun,muffin_bun,chicken_patty,vegetarian_patty,beef_patty,
                tomato,lettuce,cheddar_cheese,swiss_cheese,sauce]
    IngListWrap = [wrap,chicken_patty,vegetarian_patty,beef_patty,
                tomato,lettuce,cheddar_cheese,swiss_cheese,sauce]

    setup._get_order(1).items["Burger"][0].modify_buns(
        setup.inventory,
        sesame_bun,
        muffin_bun
    )
    setup._get_order(1).items["Burger"][0].modify_patties(
        setup.inventory,
        chicken_patty,
        vegetarian_patty,
        beef_patty
    )
    setup._get_order(1).items["Burger"][0].modify_other_ingredients(
        setup.inventory,
        tomato,
        lettuce,
        cheddar_cheese,
        swiss_cheese,
        sauce
    )
    setup._get_order(1).calculate_price()
    assert setup._get_order(1).price == 28.5
    setup._get_order(1).items["Wrap"][0].modify_wraps(
        setup.inventory,
        wrap
    )
    setup._get_order(1).items["Wrap"][0].modify_patties(
        setup.inventory,
        chicken_patty,
        vegetarian_patty,
        beef_patty
    )
    setup._get_order(1).items["Wrap"][0].modify_other_ingredients(
        setup.inventory,
        tomato,
        lettuce,
        cheddar_cheese,
        swiss_cheese,
        sauce
    ) 
    setup._get_order(1).calculate_price()
    assert setup._get_order(1).price == 38
    
    for things in setup._get_order(1).items["Wrap"][0].ingredients.values():
        for stuff in IngListWrap:
            if stuff.name in things.keys():
                assert stuff.amount == things[stuff.name].amount and stuff.additional_price == things[stuff.name].additional_price

    for things in setup._get_order(1).items["Burger"][0].ingredients.values():
        for stuff in IngListBurger:
            if stuff.name in things.keys():
                assert stuff.amount == things[stuff.name].amount and stuff.additional_price == things[stuff.name].additional_price

def test_add_more_mains_to_order(setup):
    assert setup._get_order(1).price == 38
    setup.add_items_in_orders(1,setup.get_item("Burger"),setup.get_item("Wrap"))
    setup.display_order(1)
    assert len(setup._get_order(1).items['Burger']) == 2
    assert len(setup._get_order(1).items['Wrap']) == 2

def test_modify_mains_2_cant_add_more_than_max(setup):
    #Creating Ingredients
    sesame_bun = Ingredient(name="Sesame Bun", amount=2, additional_price=1)
    muffin_bun = Ingredient(name="Muffin Bun", amount=2, additional_price=1)
    wrap = Ingredient(name = "Wrap", amount= 3, additional_price=1)
    # patties
    chicken_patty = Ingredient(name="Chicken Patty", amount=2, additional_price=2)
    vegetarian_patty = Ingredient(name="Vegetarian Patty",amount=1, additional_price=2)
    beef_patty = Ingredient(name="Beef Patty",amount=1,additional_price=2)
    # other
    tomato = Ingredient(name="Tomato", amount=1, additional_price=0.2)
    lettuce = Ingredient(name="Lettuce", amount=1, additional_price=0.2)
    cheddar_cheese = Ingredient(name = "Cheddar Cheese", amount=1, additional_price= 0.5)
    swiss_cheese = Ingredient(name = "Swiss Cheese", amount = 1, additional_price= 0.5)
    sauce = Ingredient(name = "Tomato Sauce", amount= 1, additional_price=0.1)

    IngListBurger = [sesame_bun,muffin_bun,chicken_patty,vegetarian_patty,beef_patty,
                tomato,lettuce,cheddar_cheese,swiss_cheese,sauce]

    setup._get_order(1).items["Burger"][1].modify_buns(
        setup.inventory,
        sesame_bun,
        muffin_bun
    )
    setup._get_order(1).items["Burger"][1].modify_patties(
        setup.inventory,
        chicken_patty,
        vegetarian_patty,
        beef_patty
    )
    setup._get_order(1).items["Burger"][1].modify_other_ingredients(
        setup.inventory,
        tomato,
        lettuce,
        cheddar_cheese,
        swiss_cheese,
        sauce
    )
    setup.display_order(1)
    setup._get_order(1).calculate_price()
    # Second burger should reject beef patty (amount of beef patty in burger should be nan)
    for things in setup._get_order(1).items["Burger"][1].ingredients.values():
        for stuff in IngListBurger:
            if stuff.name in things.keys():
                if stuff.name == 'Beef Patty':
                    assert(isNaN(things[stuff.name].amount))
                else:
                    assert stuff.amount == things[stuff.name].amount and stuff.additional_price == things[stuff.name].additional_price
    assert(setup._get_order(1).price == 65.5)

def test_check_out_simple(setup):
    assert(not setup._get_order(1).is_payed)
    setup.checkout(1)
    assert(setup._get_order(1).is_payed)
    setup.display_order(1)

def test_inventory_simple(setup):
    assert(setup.inventory.get_ingredient('Lettuce').amount == 200-3*30)
    assert(setup.inventory.get_ingredient('Nugget').amount == 25)
    assert(setup.inventory.get_ingredient('Fries').amount == 300-125)
    assert(setup.inventory.get_ingredient('Tomato Sauce').amount == 100-3)
    assert(setup.inventory.get_ingredient('Swiss Cheese').amount == 100-3)
    assert(setup.inventory.get_ingredient('Cheddar Cheese').amount == 100-3)
    assert(setup.inventory.get_ingredient('Tomato').amount == 100-3)
    assert(setup.inventory.get_ingredient('Chicken Patty').amount == 100-4)
    assert(setup.inventory.get_ingredient('Vegetarian Patty').amount == 100-3)
    assert(setup.inventory.get_ingredient('Beef Patty').amount == 100-2)
    assert(setup.inventory.get_ingredient('Sesame Bun').amount == 100-3)
    assert(setup.inventory.get_ingredient('Muffin Bun').amount == 100-3)
    assert(setup.inventory.get_ingredient('Wrap').amount == 100-2)

def test_staff_mark_order(setup):
    order1 = setup._get_order(1)
    assert(not order1.is_prepared)
    setup.update_order(1,'Kanadech','4568')
    assert(order1.is_prepared)

