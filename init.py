from src.order_system import OrderSystem
from src.system_creator import *


def bootstrap_system():

    system = create_save_system(
        mains=create_mains_menu("docs/Menus.csv"),
        sides=create_sides_menu("docs/Menus.csv"),
        drinks=create_drinks_menu("docs/Menus.csv"),
        inventory=create_inventory("docs/Inventory.csv"),
        staff_system=create_staffsystem("docs/StaffSystem.csv")
    )

    return system
