from tkinter.font import names


def add(inventory, item):
    """TODO: Add a new item (dict) to the inventory (list[dict])"""
    inventory.append(item)

def remove(inventory, index):
    """TODO: Remove item (dict) in the given index (int) of inventory"""
    inventory.pop(index)

def read(inventory, index):
    """TODO: Return the item (dict) in the given index (int) of inventory"""
    return inventory[index]

def show(inventory):
    """TODO: Print the items and their details line-by-line"""
    print("Inventory:")

def main():
    running = True
    inventory = []

    while running:
        command = input("Command: ")
        if command == "add":
            # TODO: Use add command"""
            name = input("Item Name: ")
            info = input("Item Info: ")
            cost = int(input("Item Cost: "))
            item = { 'Name': name, 'Info': info, 'Cost': cost }
            add(inventory, item)
            #pass
        elif command == "remove":
            #  TODO: Use remove command"""
            pass
        elif command == "read":
            # TODO: Use read command"""

            pass
        elif command == "show":
            # TODO: Use show command"""
            # itsearch = input("Enter Item to Search: ")
            # search1 = inventory.get(itsearch)
            #show(inventory)
            #pass
            print(inventory)
        elif command == "exit":
            running = False


main()
