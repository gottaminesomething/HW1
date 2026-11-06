import itemObject as io
import difflib
from pathlib import Path

inventoryFile = "inventory.txt"

Path(inventoryFile).touch(exist_ok=True)
def save_list_items(inventory, filename=inventoryFile):

	with open(filename, "w") as f:

		for x in inventory:
			f.write(x.name + "|" + x.category + "|" + str(x.quantity) + "\n")

def load_list_items(inventory, filename=inventoryFile):
	with open(filename) as f:
		print("FILE READ")

		for line in f:
			parts = line.split("|")
			inventory.append(io.item(parts[0],parts[1], int(parts[2])))

def search_inventory(inventory, obType, search):
	if obType == "1": #name
		close_matches = difflib.get_close_matches(search, [item.name for item in inventory])
		return(close_matches)
	elif obType == "2": #Category
		close_matches = difflib.get_close_matches(search, [item.category for item in inventory])
		return(close_matches)
	elif obType == "3": #Quantity
		close_matches = difflib.get_close_matches(search, [str(item.quantity) for item in inventory])
		return(close_matches)
	else:
		print("Invalid option.")

def update_quantity(inventory, changed, newNumber):
	
	if changed.isdigit():
		changed = int(changed)
	if newNumber.isdigit():
		newNumber = int(newNumber)
	else:
		return False

	if changed < 1 or changed > len(inventory):
		print("That item number does not exist")
		return False
	if newNumber < 0:
		print("the quantity cant be less than 0")
		return False

	inventory[changed - 1].quantity = newNumber 
	return True

def remove_item(inventory, rm):
		if rm == "back":
			print("returning to main menu")
			return False
		if not rm.isdigit():
			print("please enter a valid task number.")
			return False
		
		Irm = int(rm)
		if Irm < 1 or Irm > len(inventory):
			print("item does not exist.")
			return False
		
		inventory.pop(Irm - 1)
		print("task removed successfully.")
		return True

def inventory_summary(inventory):
	print("Inventory Summary")
	print("Unique items: " + str(len(inventory)))
	total = 0
	lowStock = 0
	category_dict = {}
	for i in inventory:
		total +=  i.quantity
		if i.quantity < 5:
			lowStock += 1
		if i.category.lower() not in category_dict:
			category_dict.update({str(i.category.lower()) : 1})
		else:
			category_dict[str(i.category.lower())] += 1
	
	print("Total quantity: " + str(total))
	print("Low stock items: " + str(lowStock))
	print()
	for key, value in category_dict.items():
		print(key + ":",value)



def menu(inventory):
	load_list_items(inventory)

	while True:
		print("1. View Inventory")
		print("2. Add an item")
		print("3. Update an item quantity")
		print("4. remove an item")
		print("5. Search Inventory")
		print("6. view inventory summary")
		print("7. Quit")

		choice = input("Choose an option: ")

		if choice == "1": #view inventory
			if inventory:
				for number, x in enumerate(inventory, start=1):
					print(f"{number}. {x}")
					print("----------------------")
			else:
				print("List is empty")
   
		elif choice == "2": #add an item
			name = input("Item name: ")
			category = input("Item category: ")
			while True:
				quantity = input("Item quantity: ")
				if quantity.isdigit():
					quantity = int(quantity)
					break
			inventory.append(io.item(name, category, quantity))
			print("Item added.")
			save_list_items(inventory)
			print("Items saved.")
	   
		elif choice == "3": #update item quantity
			while True:
				changed = input("input item entry number: ")
				newNumber = input("input the new quantity: ")
				if update_quantity(inventory, changed, newNumber):
					break

			save_list_items(inventory)        
		
		elif choice == "4": #remove an item
			while True:
				rm = input("input item entry number or input 'back' to return: ")
				if rm == "back":
					break

				if remove_item(inventory, rm):
					break
			save_list_items(inventory)
		
		elif choice == "5": #search inventory
			print("1. Name\n" \
				"2. Category\n" \
				"3. Quantity")
			obType = input("enter the filter(number 1, 2, or 3): ")
			search = input("Search for: ")
			print(search_inventory(inventory, obType, search))
		elif choice == "6": #view inventory summary
			print("----------------------")
			inventory_summary(inventory)
			print("----------------------")
		elif choice == "7": #exit
			break
		else:
			print("Invalid option.")

if __name__ == "__main__":
	menu(io.inventory)
