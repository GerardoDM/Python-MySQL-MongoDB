


# from consolemenu import *
# from consolemenu.items import *

# array = ['uno', 'dos', 'tres']
# array2 = tuple(array)
# # Create the menu
# menu = ConsoleMenu("Seleccione una compañia")

# # Create some items

# # A SelectionMenu constructs a menu from a list of strings
# menu_item = MenuItem(array2)

# # Once we're done creating them, we just add the items to the menu

# menu.append_item(menu_item)

# # Finally, we call show to show the menu and allow the user to interact
# menu.show()

array = ['UNO', 'DOS', 'TRES']
print(array)

company = input("Ingrese nombre de la compañia disponible ").upper()
print(company)

if company in array:
    print("Excelente")