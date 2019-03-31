from menu import Menu
from item import *
from ingredient import *
from inventory import Inventory
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
            ]
        for row in reader:
            ingredient = Ingredient(
                row["Ingredient"],
                float(row["Starting"]),
                row["Unit"]
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
            ]
        for row in reader:
            ingredient = Ingredient(
                row["Ingredient"],
                float(row["Starting"]),
                row["Unit"]
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
            sides_menu.add_items(drink)
            
        # print(sides_menu)
    menu_dict = {1:main_menu,2:drinks_menu,3:sides_menu}
    return menu_dict
    
if __name__ == "__main__":
    menu_dict = create_menu()
    with open('full_order.dat','wb') as f:
        pickle.dump(menu_dict,f,pickle.HIGHEST_PROTOCOL)
    print("Unpickling")
    with open('full_order.dat','rb') as f:
        full_order = pickle.load(f)
    print(full_order[1])
    print(full_order[2])
    print(full_order[3])