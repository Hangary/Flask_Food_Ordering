from OrderSystem import *

def setup():
    
    # Mains menu
    burger = Main("Burger", 10)
    main_menu = Menu("Main")
    main_menu.add_items(burger)

    # Sides menu
    fries = Side("Fries", 7)
    side_menu = Menu("Side")
    side_menu.add_items(fries)

    # Drink menus
    coke_zero = Drink("Coke Zero", 2.5)
    coke_diet = Drink("Coke Diet", 2.5) 
    drink_menu = Menu("Drink")
    drink_menu.add_items(coke_diet, coke_zero)

    # system
    menu = {
        "Main":     main_menu,
        "Side":     side_menu,
        "Drink":    drink_menu
    }
    system = OrderSystem(menu, None)
    return system

def test_OrderSystem_menu():
    s = setup()
    s.display_menu("Drink")
    s.display_menu("Wrong name")

def test_OrderSystem_order():
    s = setup()
    order = Order(1)
    order.add_items(s.get_item("Burger"), s.get_item("Fries"), s.get_item("Coke Zero"))
    print(order)
    s.display_menu("Drink")
    s.display_menu("DrinkandMains")

if __name__ == "__main__":
    test_OrderSystem_order()
