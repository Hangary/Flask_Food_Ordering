from OrderSystem import *


def setup():

    BURGER_BASE_PRICE = 10
    MAX_BUNS = 3

    WRAP_BASE_PRICE = 9
    MAX_WRAP = 3

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
    Mains initializer
    '''

    burger = Main("Burger", BURGER_BASE_PRICE)
    burger.add_ingredients(sesame_bun, muffin_bun,
                           chicken_patty, vegetarian_patty, tomato, lettuce)

    wrap = Main("Wrap", WRAP_PRICE)

    wrap.add_ingredients()

    mains_menu = Menu("Mains")
    mains_menu.add_items(burger)

    # system
    menu = {
        "Mains":     mains_menu,
        "Sides":     sides_menu,
        "Drinks":    drinks_menu
    }
    system = OrderSystem(menu, None)
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


if __name__ == "__main__":
    test_OrderSystem_order()
