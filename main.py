import itemObject as io
import difflib
inventoryFile = "inventory.txt"

def save_list_items():
    print("SAVE FUNCTION STARTED")

    with open(inventoryFile, "w") as f:
        print("FILE OPENED")

        for x in io.inventory:
            print("SAVE LOOP RAN")
            f.write(x.name + "|" + x.category + "|" + str(x.quantity) + "\n")

def load_list_items(): #TODO add functionality to read off of various inventories - not required, for fun
  with open(inventoryFile) as f:
        print("FILE READ")

        for line in f:
            print("LOAD LOOP RAN")
           # line = f.readline()
            parts = line.split("|")
            io.inventory.append(io.item(parts[0],parts[1], int(parts[2])))


#could you send out an announcement saying whats going to be on the exam?
#i wont easily remember the topics talked about in today's class



def search_inventory():
    print("1. Name\n" \
    "2. Category\n" \
    "3. Quantity")
    obType = input("enter the filter: ")
    search = input("Search for: ")
    if obType == "1": #name
        close_matches = difflib.get_close_matches(search,io.inventory.name)
        pass
    elif obType == "2": #Category
        pass
    elif obType == "3": #Quantity
        pass
    else:
        print("Invalid option.")
    pass

def menu():
    load_list_items()

    while True:
        #TODO update item quantity
        #TODO remove an item
        #TODO search inventory
        #TODO view inventory summary
        print("\n1. Add an item")
        print("2. Search Inventory")
        print("3. View Inventory")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Item name: ")
            category = input("Item category: ")
            quantity = int(input("Item quantity: "))
            io.inventory.append(io.item(name, category, quantity))
            print("Item added.")
            save_list_items()
            print("Items saved.")
        elif choice == "2":
            search_inventory()
            pass
        elif choice == "3":
            for x in io.inventory:
                print(x)
        elif choice == "4":
            break
        else:
            print("Invalid option.")

menu()
