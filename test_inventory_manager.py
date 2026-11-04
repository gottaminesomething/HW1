import pytest
from main import *
from types import SimpleNamespace as item
def test_load_inventory_manager_and_as_int(tmp_path):
	# Arrange
	inventory_file = tmp_path / "inventory.txt"
	inventory_file.write_text("apple|fruit|10\nBananna|fruit|5")
	inventory = []
	
	# Act
	load_list_items(inventory, inventory_file)

	# Assert
	assert [str(i) for i in inventory] == ["apple, fruit, 10", "Bananna, fruit, 5"]

def test_empty_load_list_items(tmp_path):
	inventory_file = tmp_path / "inventory.txt"
	inventory_file.touch()
	inventory = []

	# Act
	load_list_items(inventory, inventory_file)

	# Assert
	assert inventory == []

def test_load_list_items_EmptyLine(tmp_path):
	# Arrange
	inventory_file = tmp_path / "inventory.txt"
	inventory_file.write_text("apple|fruit|10\nBananna|fruit|5\n")
	inventory = []
	
	# Act
	load_list_items(inventory, inventory_file)

	# Assert
	assert [str(i) for i in inventory] == ["apple, fruit, 10", "Bananna, fruit, 5"]

def test_save_multiple_items(tmp_path):
	# Arrange

	inventory_file = tmp_path / "inventory.txt"
	inventory_file.write_text("apple|fruit|10\nbananna|fruit|5")
	inventory = [
		item(name="apple", category="fruit", quantity=10),
		item(name="bananna", category="fruit", quantity=5),
		item(name="orange", category="fruit", quantity=15)
		
	]
	expected = "apple|fruit|10\nbananna|fruit|5\norange|fruit|15\n"

	# Act
	save_list_items(inventory, inventory_file)

	# Assert
	assert inventory_file.read_text() == expected

def test_save_empty_inventory(tmp_path):
	# Arrange

	inventory_file = tmp_path / "inventory.txt"
	inventory_file.write_text("apple|fruit|10\nbananna|fruit|5")
	inventory = []
	expected = ""

	# Act
	save_list_items(inventory, inventory_file)

	# Assert
	assert inventory_file.read_text() == expected

def test_save_then_load_inventory(tmp_path):
	# Arrange

	inventory_file = tmp_path / "inventory.txt"
	inventory_file.write_text("apple|fruit|10\nbananna|fruit|5")
	inventory = [
		item(name="apple", category="fruit", quantity=10),
		item(name="bananna", category="fruit", quantity=5),
		item(name="orange", category="fruit", quantity=15)

	]
	expected = "apple|fruit|10\nbananna|fruit|5\norange|fruit|15\n"

	# Act
	save_list_items(inventory, inventory_file)
	inventory = []
	load_list_items(inventory, inventory_file)

	# Assert
	assert [str(i) for i in inventory] == ["apple, fruit, 10", "bananna, fruit, 5", "orange, fruit, 15"]