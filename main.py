import itemObject as io
import difflib
inventoryFile = "inventory.txt"
if not inventoryFile:
    f = open(inventoryFile, "a")
    pass
def save_list_items():

    with open(inventoryFile, "w") as f:

        for x in io.inventory:
            f.write(x.name + "|" + x.category + "|" + str(x.quantity) + "\n")

def load_list_items(): #TODO add functionality to read off of various inventories - not required, for fun
  with open(inventoryFile) as f:
        print("FILE READ")

        for line in f:
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
        close_matches = difflib.get_close_matches(search, [item.name for item in io.inventory])
        print(close_matches)
        pass
    elif obType == "2": #Category
        close_matches = difflib.get_close_matches(search, [item.category for item in io.inventory])
        print(close_matches)
    elif obType == "3": #Quantity
        close_matches = difflib.get_close_matches(search, [item.quantity for item in io.inventory])
        print(close_matches)
    else:
        print("Invalid option.")
    pass
def update_quantity():
    changed = int(input("input item entry number: "))
    newNumber = int(input("input the new quantity: "))
    if changed < 1 or changed > len(io.inventory):
        print("That item number does not exist")
        return False

    io.inventory[changed - 1].quantity = newNumber 

def remove_item():
    while True:
        rm = input("input item entry number or input 'back' to return: ")
        Irm = int(rm)
        if rm == "back":
            print("returning to main menu")
            return False
        elif not rm.isdigit():
            print("please enter a valid task number.")
        elif Irm < 1 or Irm > len(io.inventory):
            print("item does not exist.")
        else:
            io.inventory.pop(Irm - 1)
            print("task removed successfully.")
            return False
    pass


def menu():
    load_list_items()

    while True:
        #TODO remove an item
        #TODO view inventory summary
        print("1. View Inventory")
        print("2. Add an item")
        print("3. Update an item quantity")
        print("4. remove an item")
        print("5. Search Inventory")
        print("6. view inventory summary --unfinished")
        print("7. load different inventory -- unfinished")
        print("8. Quit")

        choice = input("Choose an option: ")

        if choice == "1": #view inventory
            if io.inventory:
                for number, x in enumerate(io.inventory, start=1):
                    print(f"{number}. {x}")
                    print("----------------------")
            else:
                print("List is empty")
        elif choice == "2": #add an item
            name = input("Item name: ")
            category = input("Item category: ")
            quantity = int(input("Item quantity: "))
            io.inventory.append(io.item(name, category, quantity))
            print("Item added.")
            save_list_items()
            print("Items saved.")
        elif choice == "3": #update item quantity
            update_quantity()
            save_list_items()        
        elif choice == "4": #remove an item
            remove_item()
            save_list_items()
        
        elif choice == "5": #search inventory
            search_inventory()
            pass
        elif choice == "6": #view inventory summary
            pass
        elif choice == "7": #load different inventory
            pass
        elif choice == "8": #exit
            break
        else:
            print("Invalid option.")

menu()
