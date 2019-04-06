from ingredient import Ingredient
from inventory import Inventory
import pytest
from system_creator import create_inventory

@pytest.fixture
def test_fixture():
    inventory = create_inventory("docs/Inventory.csv")
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