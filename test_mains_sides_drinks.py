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

def test_mains():
    s = setup()
    # create a new order
    order = Order(order_id=1)
    # add burger into the order
    order.add_items(s.get_item("Burger"))

    # modify the buns of the burger
    order.items["Burger"].modify_buns(
        s.inventory,
        Ingredient(name="Sesame Bun", amount=1, additional_price=1),
        Ingredient(name="Muffin Bun", amount=1, additional_price=1)
    )
    # modify the patties of the burger
    order.items["Burger"].modify_patties(
        s.inventory,
        Ingredient(name="Chicken Patty", amount=2, additional_price=3),
        Ingredient(name="Vegetarian Patty", amount=1, additional_price=2)
    )
    # modify other ingredients of the burger
    order.items["Burger"].modify_other_ingredients(
        s.inventory,
        Ingredient(name="tomato", amount=1, additional_price=0.5),
        Ingredient(name="lettuce", amount=0, additional_price=0.3)
    )

    # review this burger
    order.items['Burger'].review()




if __name__ == "__main__":
    test_mains()