from OrderSystem import *

def setup():
    
    # Mains menu
    burger = Main("Burger", 10)
    mains_menu = Menu("Mains")
    mains_menu.add_items(burger)

    # Sides menu
    fries = Side("Fries", 7)
    sides_menu = Menu("Sides")
    sides_menu.add_items(fries)

    # Drink menus
    coke_zero = Drink("Coke Zero", 2.5)
    coke_diet = Drink("Coke Diet", 2.5) 
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

def test_OrderSystem_menu():
    s = setup()
    s.display_menu("Drinks")
    s.display_menu("Wrong name")

def test_OrderSystem_order():
    s = setup()
    order = Order(1)
    burger = s.get_item("Burger")
    print(burger)
    order.add_items(s.get_item("Burger"), s.get_item("Fries"), s.get_item("Coke Zero"))
    print(order)

if __name__ == "__main__":
    test_OrderSystem_order()
