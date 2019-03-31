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
    ### Creating Mains Menu (Need to add Wrap later)
    
    burger = Main("Burger", BURGER_BASE_PRICE)
    inven = Inventory()
    with open('main.csv') as f:
        reader = csv.DictReader(f)
        COLUMNS = [
            'Ingredient'
            'Stock Unit'
            'Unit'
            'price'
            ]
        for row in reader:
            ingredient = Ingredient(
                row["Ingredient"],
                100,
                row["Unit"],
                float(row["price"])
            )
            burger.calculate_price() #TypeError: unsupported operand type(s) for +=: 'int' and 'str'
            burger.add_ingredients(ingredient)
            inven.add_new_ingredients(ingredient)
    main_menu = Menu("Mains")
    main_menu.add_items(burger)
    print(burger)
    print(main_menu)

    ### Creating Drinks Menu
    drinks_menu = Menu("Drinks")
    with open('drink.csv') as d:
        reader = csv.DictReader(d)
        COLUMNS = [
            'Ingredient'
            'Stock Unit'
            'Unit'
            'price'
            ]
        for row in reader:
            ingredient = Ingredient(
                row["Ingredient"],
                100,
                row["Unit"],
                float(row["price"])
            )
            drink = Drink(row["Ingredient"],float(row["price"]))
            drink.add_ingredients(ingredient)
            drinks_menu.add_items(drink)
            inven.add_new_ingredients(ingredient)
        print(drinks_menu)
    
    menu_dict = {1:main_menu,2:drinks_menu}
    return menu_dict
    
if __name__ == "__main__":
    menu_dict = create_menu()
    print(menu_dict)
    print(menu_dict[1])
    with open('full_order.dat','wb') as f:
        pickle.dump(menu_dict,f,pickle.HIGHEST_PROTOCOL)
    print("Try loading")
    with open('full_order.dat','rb') as f:
        full_order = pickle.load(f)
    print(full_order[1])