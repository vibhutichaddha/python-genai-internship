inventory = {}
def add_product(name, price, quantity):
    inventory[name]={
        "price": price,
        "quantity": quantity
    }
def update_quantity(name, quantity):
    if name in inventory:
        inventory[name]["quantity"] = quantity
    else:
        print(f"Product {name} not found in inventory.")
def search_product(name):
    if name in inventory:
        return inventory[name]
    else:
        print(f"Product {name} not found in inventory.")
def remove_product(name):
    if name in inventory:
        del inventory[name]
    else:
        print(f"Product {name} not found in inventory.")
def display_inventory():
    for name, details in inventory.items():
        print(name,":",details)
add_product("Laptop", 60000, 10)
add_product("Mouse", 700, 12)
update_quantity("Laptop",5)
print ("Search:",search_product("Laptop"))
display_inventory()
remove_product("Mouse")
print("After removing product:")
display_inventory()