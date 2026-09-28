import itemObject as io
inventoryFile = "inventory.txt"

def save_list_items():
    print("SAVE FUNCTION STARTED")

    with open(inventoryFile, "w") as f:
        print("FILE OPENED")

        for x in io.inventory:
            print("SAVE LOOP RAN")
            f.write(x.name + "|" + x.category + "|" + str(x.quantity) + "\n")

def load_list_items():
  with open(inventoryFile) as f:
        print("FILE READ")

        for line in f:
            print("LOAD LOOP RAN")
           # line = f.readline()
            parts = line.split("|")
            io.inventory.append(io.item(parts[0],parts[1], int(parts[2])))

def menu():
    load_list_items()

    while True:
        print("\n1. Make item")
        print("2. Save items")
        print("3. Print items")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Item name: ")
            category = input("Item category: ")
            quantity = int(input("Item quantity: "))
            io.inventory.append(io.item(name, category, quantity))
            print("Item added.")
        elif choice == "2":
            save_list_items()
            print("Items saved.")
        elif choice == "3":
            for x in io.inventory:
                print(x)
        elif choice == "4":
            break
        else:
            print("Invalid option.")

menu()
