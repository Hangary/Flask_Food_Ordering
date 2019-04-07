from ingredient import Ingredient
from inventory import Inventory
from system_creator import create_inventory
import pytest


@pytest.fixture(scope='module')
def test_fixture():
    inventory = create_inventory("../docs/Inventory.csv")
    return inventory

def test_get_valid_ingredient(test_fixture):
    ingredient = test_fixture.get_ingredient("Fries")
    assert(ingredient.name == "Fries")
    assert(ingredient.amount == 300)
    assert(ingredient.is_soldout == False)
    assert(ingredient.unit == "g")

    ingredient = test_fixture.get_ingredient("Coke")
    assert(ingredient.name == "Coke")
    assert(ingredient.amount == 1500)
    assert(ingredient.is_soldout == False)
    assert(ingredient.unit == "ml")

    ingredient = test_fixture.get_ingredient("Cheddar Cheese")
    assert(ingredient.name == "Cheddar Cheese")
    assert(ingredient.amount == 100)
    assert(ingredient.is_soldout == False)
    assert(ingredient.unit == "slice")

def test_get_invalid_ingredient(test_fixture):
    try:
        test_fixture.get_ingredient("BAD NUGGET")
        assert(False)
    except KeyError:
        assert(True)
        
def test_changing_stock_number(test_fixture):
    test_fixture.update_stock("Fries",100)
    assert test_fixture.get_ingredient("Fries").amount == 400
    test_fixture.update_stock("Ice",-600)
    assert test_fixture.get_ingredient("Fries").amount == 400

def test_availability(test_fixture):
    test_fixture.update_stock("Lettuce",-6)
    assert test_fixture.get_ingredient("Lettuce").amount == 20
    assert test_fixture.is_available("Lettuce",1) == False
    assert "Lettuce" in test_fixture.display_unavailable_ingredients()
    test_fixture.update_stock("OrangeJuice",-950)
    assert test_fixture.get_ingredient("OrangeJuice").amount == 50
    assert "OrangeJuice" and "Lettuce" in test_fixture.display_unavailable_ingredients()
    print(test_fixture.display_unavailable_ingredients())
    #assert(0)