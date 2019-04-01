from menu import Menu
from item import *
from ingredient import *
from inventory import Inventory
from OrderSystem import *
import csv
import pickle
BURGER_BASE_PRICE = 10
WRAP_BASE_PRICE = 9
MAX_BUNS = 4
MAX_PATTIES = 3
'''
TODO:
This should be a helper function,
which will read data from a file and output a system with correct menus and inventory.
'''

def create_menu():
    
    ### Creating Mains Menu Burger and Wrap
    burger = Main("Burger", BURGER_BASE_PRICE)
    wrap = Wrap("Wrap",WRAP_BASE_PRICE)
    inven = Inventory()
    with open('main.csv') as f:
        reader = csv.DictReader(f)
        COLUMNS = [
            'Ingredient'
            'Stock Unit'
            'Unit'
            'price'
            'For'
            ]
        for row in reader:
            ingredient = Ingredient(
                row["Ingredient"],
                100,
                row["Unit"],
                float(row["price"])
            )
            if row['For'] == "BW":
                burger.add_ingredients(ingredient)
                wrap.add_ingredients(ingredient)
            elif row['For'] == "B":
                burger.add_ingredients(ingredient)
            else:
                wrap.add_ingredients(ingredient)
            inven.add_new_ingredients(ingredient)

    main_menu = Menu("Mains")
    main_menu.add_items(burger,wrap)
    # print(burger)
    # print(wrap)
    # print(main_menu)

    ### Creating Drinks Menu
    drinks_menu = Menu("Drinks")
    with open('drink_ing.csv') as d:
        reader = csv.DictReader(d)
        COLUMNS = [
            'Ingredient'
            'Unit'
            'Starting'
            'Min_Selling'
            ]
        for row in reader:
            ingredient = Ingredient(
                row["Ingredient"],
                float(row["Starting"]),
                row["Unit"],
                min_selling=float(row['Min_Selling'])
            )
            inven.add_new_ingredients(ingredient)
    with open('drink.csv') as d1:
        reader = csv.DictReader(d1)
        COLUMNS = [
            'Item'
            'Multiplier'
            'Price'
            'Use'
            ]
        for row in reader:
            drink = Drink(row["Item"],float(row["price"]),float(row["Multiplier"]))
            drink.add_ingredients(inven.get_ingredient(row['Use']))
            drinks_menu.add_items(drink)
            
        # print(drinks_menu)
    
    ### Creating Drinks Menu
    sides_menu = Menu("Sides")
    with open('side_ing.csv') as d:
        reader = csv.DictReader(d)
        COLUMNS = [
            'Ingredient'
            'Unit'
            'Starting'
            'Min_Selling'
            ]
        for row in reader:
            ingredient = Ingredient(
                row["Ingredient"],
                float(row["Starting"]),
                row["Unit"],
                min_selling=float(row['Min_Selling'])
            )
            inven.add_new_ingredients(ingredient)
    with open('side.csv') as d1:
        reader = csv.DictReader(d1)
        COLUMNS = [
            'Item'
            'Multiplier'
            'Price'
            'Use'
            ]
        for row in reader:
            side = Side(row["Item"],float(row["price"]),float(row["Multiplier"]))
            side.add_ingredients(inven.get_ingredient(row['Use']))
            sides_menu.add_items(side)
            
        # print(sides_menu)
    menu_dict = {"Mains":main_menu,"Sides":sides_menu,"Drinks":drinks_menu}
    system = OrderSystem(menu_dict,inven)
    return system
    
if __name__ == "__main__":
    # menu_dict = create_menu()
    # with open('full_order.dat','wb') as f:
    #     pickle.dump(menu_dict,f,pickle.HIGHEST_PROTOCOL)
    # print("Unpickling")
    # with open('full_order.dat','rb') as f:
    #     full_order = pickle.load(f)
    # print(full_order[1])
    # print(full_order[2])
    # print(full_order[3])
    system = create_menu()
    with open('full_order.dat','wb') as f:
        pickle.dump(system,f,pickle.HIGHEST_PROTOCOL)
    system.make_order()
    print("Showing sides menu")
    system.display_menu("Sides")
    SF = system.get_item("Small Fries")
    MF = system.get_item("Med Fries")
    LF = system.get_item("Large Fries")
    N3 = system.get_item("Nugget 3 pack")
    N6 = system.get_item("Nugget 6 pack")
    print("Ordering Fries")
    system.add_items_in_orders(1,SF,MF,LF,SF)
    system.display_order(1)
    print("Ordering Nuggets")
    system.add_items_in_orders(1,N6,N3,N6,N3,N6,N3)
    system.display_order(1)
    print("Amount of Fries left {}".format(system.inventory.get_ingredient('Fries').amount))
    print("Amount of Nuggets left {}".format(system.inventory.get_ingredient('Nugget').amount))
    print("Out of Stock",system.inventory.display_unavailable_ingredients())
    
    print("Showing drinks menu")
    system.display_menu("Drinks")
    print("Ordering Juice")
    OS = system.get_item("OrangeJuice_Small")
    OD = system.get_item("OrangeJuice_Medium")
    system.add_items_in_orders(1,OS,OS,OD,OD)
    print("Ordering Coke")
    CB = system.get_item("Coke Bottle")
    CC = system.get_item("Coke Can")
    system.add_items_in_orders(1,CC,CB,CC,CB)
    system.display_order(1)
    print("Amount of Coke left {}".format(system.inventory.get_ingredient('Coke').amount))
    print("Amount of OrangeJuice left {}".format(system.inventory.get_ingredient('OrangeJuice').amount))
    print("Out of Stock",system.inventory.display_unavailable_ingredients())