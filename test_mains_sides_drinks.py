from OrderSystem import *
from inventory import *
from system_creator import *

def setup():
    '''
    system initializer
    '''
    system = create_save_system(
        mains=create_mains_menu("docs/Menus.csv"),
        sides=create_sides_menu("docs/Menus.csv"),
        drinks=create_drinks_menu("docs/Menus.csv"),
        inventory=create_inventory("docs/Inventory.csv")
    )
    
    return system

def test_mains():
    s = setup()
    # create a new order
    order = Order(order_id=1)
    # add burger into the order
    order.add_items(s.get_item("Burger"))

    # modify the buns of the burger
    order.items["Burger"][0].modify_buns(
        s.inventory,
        Ingredient(name="Sesame Bun", amount=1, additional_price=1),
        Ingredient(name="Muffin Bun", amount=1, additional_price=1)
    )
    # modify the patties of the burger
    order.items["Burger"][0].modify_patties(
        s.inventory,
        Ingredient(name="Chicken Patty", amount=2, additional_price=3),
        Ingredient(name="Vegetarian Patty", amount=1, additional_price=2)
    )
    # modify other ingredients of the burger
    order.items["Burger"][0].modify_other_ingredients(
        s.inventory,
        Ingredient(name="Tomato", amount=1, additional_price=0.5),
        Ingredient(name="Lettuce", amount=0, additional_price=0.3)
    )

    # review this burger
    order.items['Burger'][0].review()


def test_mains2():

    system = setup()

    system.make_order()

    burger = system.get_item("Burger")
    wrap = system.get_item("Wrap")

    system.add_items_in_orders(1, burger, wrap)
    
    # buns
    sesame_bun = Ingredient(name="Sesame Bun", additional_price=1)
    muffin_bun = Ingredient(name="Muffin Bun", additional_price=1)
    # patties
    chicken_patty = Ingredient(name="Chicken Patty", additional_price=3)
    vegetarian_patty = Ingredient(name="Vegetarian Patty", additional_price=2)
    # other
    tomato = Ingredient(name="tomato", additional_price=0.5)
    lettuce = Ingredient(name="lettuce", additional_price=0.3)

    system._get_order(1).items["Burger"][0].modify_buns(
        system.inventory,
        bun
    )
    system._get_order(1).items["Burger"][0].modify_patties(
        system.inventory,
        patty
    )
    system._get_order(1).items["Wrap"][0].modify_wraps(
        system.inventory,
        wrap
    )
    system._get_order(1).items["Burger"][0].modify_other_ingredients(
        system.inventory,
        tomato, cheese
    )

    system._get_order(1).calculate_price()
    system.display_order(1)

    print("Amount of Bun left {}".format(
        system.inventory.get_ingredient('Bun').amount))
    print("Amount of Wrap left {}".format(
        system.inventory.get_ingredient('Wrap').amount))
    print("Amount of Patty left {}".format(
        system.inventory.get_ingredient('Patty').amount))
    print("Amount of Tomato left {}".format(
        system.inventory.get_ingredient('Tomato').amount))
    print("Amount of Cheese left {}".format(
        system.inventory.get_ingredient('Cheese').amount))

    print("~~~~~~~~~~~~~~~~~~Showing Mains Menu~~~~~~~~~~~~~~~~")
    system.display_menu("Mains")




if __name__ == "__main__":
    test_mains()