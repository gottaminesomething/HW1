import pytest
from main import *
from types import SimpleNamespace as item

@pytest.fixture
def sample_inventory():
	return [
		item(name="apple", category="fruit", quantity=10),
		item(name="hammer", category="tool", quantity=5),
		item(name="apple", category="fruit", quantity=10),
		item(name="orange", category="fruit", quantity=15)
	]

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

def test_save_multiple_items(tmp_path, sample_inventory):
	# Arrange

	inventory_file = tmp_path / "inventory.txt"
	inventory_file.write_text("apple|fruit|10\nbananna|fruit|5")
	inventory = sample_inventory
	expected = "apple|fruit|10\nhammer|tool|5\napple|fruit|10\norange|fruit|15\n"

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

def test_save_then_load_inventory(tmp_path, sample_inventory):
	# Arrange

	inventory_file = tmp_path / "inventory.txt"
	inventory_file.write_text("apple|fruit|10\nbananna|fruit|5")
	inventory = sample_inventory
	expected = "apple|fruit|10\nhammer|tool|5\napple|fruit|10\norange|fruit|15\n"

	# Act
	save_list_items(inventory, inventory_file)
	inventory = []
	load_list_items(inventory, inventory_file)

	# Assert
	assert [str(i) for i in inventory] == ["apple, fruit, 10", "hammer, tool, 5", "apple, fruit, 10", "orange, fruit, 15"]


@pytest.mark.parametrize("obType, search, expected",[
	("1", "apple", "apple"),
	("2", "tool", "tool"),
	("3", "10", "10")
])

def test_seach_exact_item(sample_inventory, obType, search, expected):
	# Arrange
	inventory = sample_inventory
	# Act
	result = search_inventory(inventory, obType, search)


	# Assert
	assert expected in result #result_name[0] gets the first(only) element in the list and compares it as a string
	

@pytest.mark.parametrize("obType, search, expected", [
	("1", "app", "apple"),
	("1", "Apple", "apple"),
	("2", "to", "tool"),
	("3", "100", "10"),
	("3", "1", "10")
])
def test_search_partial(sample_inventory, obType, search, expected):
	# Act
	result = search_inventory(sample_inventory, obType, search)

	# Assert
	assert expected in result

	
@pytest.mark.parametrize("obType, search, expected", [
	("1", "apple", ["apple", "apple"]),
	("2", "fruit", ["fruit", "fruit", "fruit"]),
	("3", "10", ["10", "10"])
])
def test_search_duplicates(sample_inventory, obType, search, expected):
	# Act
	result = search_inventory(sample_inventory, obType, search)

	# Assert
	assert sorted(result) == sorted(expected)


@pytest.mark.parametrize("obType, search, expected", [
	("1", "Spaceship", []),
	("1", "grape", ["apple", "apple"]),
	("2", "food", []),
	("3", "8", [])
])
def test_search_no_matching_and_fuzzy(sample_inventory, obType, search, expected):
	# Act
	result = search_inventory(sample_inventory, obType, search)

	# Assert
	assert sorted(result) == sorted(expected)


@pytest.mark.parametrize("obType, search, expected", [
	("1", "", []),
	("2", "", []),
	("3", "", [])
])
def test_search_with_whitespace(sample_inventory, obType, search, expected):
	# Act
	result = search_inventory(sample_inventory, obType, search)

	# Assert
	assert result == expected



def test_remove_item(sample_inventory):
	# Arrange	
	expected = [
		item(name="hammer", category="tool", quantity=5),
		item(name="apple", category="fruit", quantity=10),
		item(name="orange", category="fruit", quantity=15)
	]
	# Act
	remove_item(sample_inventory, "1")

	# Assert
	assert [str(i) for i in sample_inventory] == [str(i) for i in expected]

def test_remove_middle(sample_inventory):
	# Arrange	
	expected = [
		item(name="apple", category="fruit", quantity=10),
		item(name="apple", category="fruit", quantity=10),
		item(name="orange", category="fruit", quantity=15)
	]
	# Act
	remove_item(sample_inventory, "2")

	# Assert
	assert [str(i) for i in sample_inventory] == [str(i) for i in expected]

def test_remove_zero(sample_inventory):
	# Arrange
	expected = [
		item(name="apple", category="fruit", quantity=10),
		item(name="hammer", category="tool", quantity=5),
		item(name="apple", category="fruit", quantity=10),
		item(name="orange", category="fruit", quantity=15)
	]
	# Act
	remove_item(sample_inventory, "0")
	# Assert
	assert [str(i) for i in sample_inventory] == [str(i) for i in expected]

def test_remove_negative(sample_inventory):
	# Arrange
	expected = [
		item(name="apple", category="fruit", quantity=10),
		item(name="hammer", category="tool", quantity=5),
		item(name="apple", category="fruit", quantity=10),
		item(name="orange", category="fruit", quantity=15)
	]
	# Act
	remove_item(sample_inventory, "-1")
	# Assert
	assert [str(i) for i in sample_inventory] == [str(i) for i in expected]

def test_remove_greater_than_list(sample_inventory):
	# Arrange
	expected = [
		item(name="apple", category="fruit", quantity=10),
		item(name="hammer", category="tool", quantity=5),
		item(name="apple", category="fruit", quantity=10),
		item(name="orange", category="fruit", quantity=15)
	]
	# Act
	remove_item(sample_inventory, "100")
	# Assert
	assert [str(i) for i in sample_inventory] == [str(i) for i in expected]

@pytest.mark.parametrize("changed, newNumber, expected", [
	("1", "5", 5), #valid item
	("2", "0", 0), #valid item at 0
	("0", "1", 0), #invalid item
	("1", "-1", 10) #invalid quantity
])
def test_update_quantity(sample_inventory, changed, newNumber, expected):
		# Act
	result = update_quantity(sample_inventory, changed, newNumber)

	# Assert
	if changed =="0":
		assert result is False
	elif int(newNumber) < 0:
		assert result is False
		assert sample_inventory[0].quantity == 10
	else:
		assert sample_inventory[int(changed) - 1].quantity == expected

def test_update_unrelated(sample_inventory):
	# Arrange
	expected = [
		item(name="apple", category="fruit", quantity=5),
		item(name="hammer", category="tool", quantity=5),
		item(name="apple", category="fruit", quantity=10),
		item(name="orange", category="fruit", quantity=15)
	]
	# Act
	update_quantity(sample_inventory, "1", "5")
	# Assert
	assert expected == sample_inventory