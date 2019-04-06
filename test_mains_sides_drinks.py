from OrderSystem import *
from inventory import *
from system_creator import *
import pickle

def setup():
    '''
    system initializer
    '''
    system = create_save_system(
        mains=create_mains_menu("docs/Menus.csv"),
        sides=create_sides_menu("docs/Menus.csv"),
        drinks=create_drinks_menu("docs/Menus.csv"),
        inventory=create_inventory("docs/Inventory.csv"),
        staff_system=create_staffsystem("docs/StaffSystem.csv")
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

    try:
        with open('full_order.dat','rb') as f:
            system = pickle.load(f)
    except FileNotFoundError:
        print("File not found creating new system")
        system = setup()
    orderID = system.make_order()
    print(orderID)
    system.add_items_in_orders(
        orderID, 
        system.get_item("Burger"), 
        system.get_item("Wrap"),
        system.get_item("Coke Can"),
        system.get_item("Coke Can"),
        system.get_item("Nugget 6 pack"),
        system.get_item("Nugget 6 pack")
    )
    
    # buns
    sesame_bun = Ingredient(name="Sesame Bun", amount=2, additional_price=1)
    muffin_bun = Ingredient(name="Muffin Bun", amount=1, additional_price=1)
    # patties
    chicken_patty = Ingredient(name="Chicken Patty", amount=3, additional_price=3)
    vegetarian_patty = Ingredient(name="Vegetarian Patty",amount=1, additional_price=2)
    # other
    tomato = Ingredient(name="Tomato", amount=2, additional_price=0.5)
    lettuce = Ingredient(name="Lettuce", amount=3, additional_price=0.2)

    '''
    Modify burger
    '''

    system._get_order(orderID).items["Burger"][0].modify_buns(
        system.inventory,
        sesame_bun,
        muffin_bun
    )
    system._get_order(orderID).items["Burger"][0].modify_patties(
        system.inventory,
        chicken_patty,
        vegetarian_patty
    )
    system._get_order(orderID).items["Burger"][0].modify_other_ingredients(
        system.inventory,
        tomato,
        lettuce
    )

    '''
    Modify Wrap
    '''

    system._get_order(orderID).items["Wrap"][0].modify_wraps(
        system.inventory,
        
    )

    system._get_order(orderID).calculate_price()
    system.display_order(orderID)
    system.checkout(orderID)

    print(f"Amount of Sesame Bun left {system.inventory.get_ingredient('Sesame Bun').amount}")
    print("Amount of Lettuce left {}".format(system.inventory.get_ingredient('Lettuce').amount))
    print("Amount of Nugget left {}".format(system.inventory.get_ingredient('Nugget').amount))
    #print("Amount of Tomato left {}".format(system.inventory.get_ingredient('Tomato').amount))
    #print("Amount of Cheese left {}".format(system.inventory.get_ingredient('Cheese').amount))

    print("~~~~~~~~~~~~~~~~~~Showing Mains Menu~~~~~~~~~~~~~~~~")
    system.display_menu("Mains")
    print(system.get_item("Burger"))
    print(system.get_item("Wrap"))
    print("Pickling system")
    with open('full_order.dat','wb') as f:
        pickle.dump(system,f,pickle.HIGHEST_PROTOCOL)


def test_persistance():
    try:
        with open('full_order.dat','rb') as f:
            system = pickle.load(f)
    except FileNotFoundError:
        print("File not Found")
        assert(False)
    for i in range(1,system.total_order+1):
        system.display_order(i)

def test_mains3():
    try:
        with open('full_order.dat','rb') as f:
            system = pickle.load(f)
    except FileNotFoundError:
        print("File not Found")
        assert(False) 

    orderID = system.make_order()
    print(orderID)
    system.add_items_in_orders(
        orderID, 
        system.get_item("Burger"), 
        system.get_item("Wrap"),
        system.get_item("Coke Can"),
        system.get_item("Coke Can"),
        system.get_item("Nugget 6 pack"),
        system.get_item("Nugget 6 pack")
    )
    
    # buns
    sesame_bun = Ingredient(name="Sesame Bun", amount=2, additional_price=1)
    muffin_bun = Ingredient(name="Muffin Bun", amount=1, additional_price=1)
    # patties
    chicken_patty = Ingredient(name="Chicken Patty", amount=3, additional_price=3)
    vegetarian_patty = Ingredient(name="Vegetarian Patty",amount=1, additional_price=2)
    # other
    tomato = Ingredient(name="Tomato", amount=2, additional_price=0.5)
    lettuce = Ingredient(name="Lettuce", amount=3, additional_price=0.2)

    '''
    Modify burger
    '''

    system._get_order(orderID).items["Burger"][0].modify_buns(
        system.inventory,
        sesame_bun,
        muffin_bun
    )
    system._get_order(orderID).items["Burger"][0].modify_patties(
        system.inventory,
        chicken_patty,
        vegetarian_patty
    )
    system._get_order(orderID).items["Burger"][0].modify_other_ingredients(
        system.inventory,
        tomato,
        lettuce
    )

    '''
    Modify Wrap
    '''

    system._get_order(orderID).items["Wrap"][0].modify_wraps(
        system.inventory,
        
    )

    system._get_order(orderID).calculate_price()
    system.display_order(orderID)
    system.checkout(orderID)
    print(f"Amount of Sesame Bun left {system.inventory.get_ingredient('Sesame Bun').amount}")
    print("Amount of Lettuce left {}".format(system.inventory.get_ingredient('Lettuce').amount))
    print("Amount of Nugget left {}".format(system.inventory.get_ingredient('Nugget').amount))
    #print("Amount of Tomato left {}".format(system.inventory.get_ingredient('Tomato').amount))
    #print("Amount of Cheese left {}".format(system.inventory.get_ingredient('Cheese').amount))


    #TODO: before first run $ rm full_order.dat
    # Unpickle the full_order.dat here
    # Checkout order_id 1
    # inspect if the inventory is being decremented correctly
    # 1st run seems ok? Modify the fucntion so that it checkout everyorder in the pending_order list
    # inspect that everyorder is in completed_order list
    # may be do some testings on your staff class here too.
   # pass
    def test_4():
        system.update_order(orderID,'Gaurang','1234')
     print(system.completed_orders)
        print(system.pending_orders)

if __name__ == "__main__":
    test_mains2()
    test_mains3()
  #  test_persistance()