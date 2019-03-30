from OrderSystem import *
from inventory import Inventory


def setup():

    BURGER_BASE_PRICE = 10
    WRAP_BASE_PRICE = 9
    MAX_BUNS = 3
    MAX_PATTIES = 3

    '''
    ingredients initializer
    '''
    # buns
    sesame_bun = Ingredient(name="Sesame Bun", additional_price=1)
    muffin_bun = Ingredient(name="Muffin Bun", additional_price=1)
    # patties
    chicken_patty = Ingredient(name="Chicken Patty", additional_price=3)
    vegetarian_patty = Ingredient(name="Vegetarian Patty", additional_price=2)
    # other
    tomato = Ingredient(name="tomato", additional_price=0.5)
    lettuce = Ingredient(name="lettuce", additional_price=0.3)

    '''
    Inventory initializer
    '''
    inventory = Inventory()
    inventory.add_new_ingredients(
        Ingredient(name="Sesame Bun", amount=100, additional_price=1),
        Ingredient(name="Muffin Bun", amount=100, additional_price=1),
        Ingredient(name="Chicken Patty", amount=100, additional_price=3),
        Ingredient(name="Vegetarian Patty", amount=100, additional_price=2),
        Ingredient(name="tomato", amount=100, additional_price=0.5),
        Ingredient(name="lettuce", amount=100, additional_price=0.3)
        )
    
    '''
    Mains initializer
    '''
    # Buger
    burger = Main("Burger", BURGER_BASE_PRICE)
    burger.add_ingredients(sesame_bun, muffin_bun,
                           chicken_patty, vegetarian_patty,
                           tomato, lettuce)
    burger.set_ingredient_limit(ingredient_name="Bun", amount=MAX_BUNS)
    burger.set_ingredient_limit(ingredient_name="Patty", amount=MAX_PATTIES)
    # Wrap
    wrap = Main("Wrap", WRAP_BASE_PRICE)
    wrap.add_ingredients(sesame_bun, muffin_bun,
                         chicken_patty, vegetarian_patty,
                         tomato, lettuce)
    burger.set_ingredient_limit(ingredient_name="Bun", amount=MAX_BUNS)
    burger.set_ingredient_limit(ingredient_name="Patty", amount=MAX_PATTIES) 
    '''
    Menu initializer
    '''
    mains_menu = Menu("Mains")
    mains_menu.add_items(burger, wrap)

    '''
    system initializer
    '''

    menu = {
        "Mains":     mains_menu,
    }
    system = OrderSystem(menu, inventory)
    return system


def test_OrderSystem_menu():
    s = setup()
    s.display_menu("Drinks")
    s.display_menu("Wrong name")


def test_OrderSystem_order():
    s = setup()
    order = Order(1)
    burger = s.get_item("Burger")
    print(burger)
    order.add_items(s.get_item("Burger"), s.get_item(
        "Fries"), s.get_item("Coke Zero"))
    print(order)

def test_mains():
    s = setup()
    order = Order(1)
    order.add_items(s.get_item("Burger"))
    order.items["Burger"].modify_buns(
        s.inventory,
        Ingredient(name="Sesame Bun", amount=1, additional_price=1),
        Ingredient(name="Muffin Bun", amount=1, additional_price=1)
    )
    order.items["Burger"].modify_patties(
        s.inventory,
        Ingredient(name="Chicken Patty", amount=2, additional_price=3),
        Ingredient(name="Vegetarian Patty", amount=1, additional_price=2)
    )
    order.items["Burger"].modify_other_ingredients(
        s.inventory,
        Ingredient(name="tomato", amount=1, additional_price=0.5),
        Ingredient(name="lettuce", amount=0, additional_price=0.3)
    )
    order.items['Burger'].review()

if __name__ == "__main__":
    test_mains()