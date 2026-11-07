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
], ids=["name", "category", "quantity"])

def test_search_exact_item(sample_inventory, obType, search, expected):
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
], ids=["partial name", "name case", "partial category", "extra digit", "partial quantity"])
def test_search_partial(sample_inventory, obType, search, expected):
	# Act
	result = search_inventory(sample_inventory, obType, search)

	# Assert
	assert expected in result

	
@pytest.mark.parametrize("obType, search, expected", [
	("1", "apple", ["apple", "apple"]),
	("2", "fruit", ["fruit", "fruit", "fruit"]),
	("3", "10", ["10", "10"])
], ids=["duplicate names", "duplicate categories", "duplicate quantities"])
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
], ids=["no name match", "fuzzy name", "no category match", "no quantity match"])
def test_search_no_matching_and_fuzzy(sample_inventory, obType, search, expected):
	# Act
	result = search_inventory(sample_inventory, obType, search)

	# Assert
	assert sorted(result) == sorted(expected)


@pytest.mark.parametrize("obType, search, expected", [
	("1", "", []),
	("2", "", []),
	("3", "", [])
], ids=["empty name", "empty category", "empty quantity"])
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
], ids=["valid quantity", "zero quantity", "invalid item", "negative quantity"])
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

@pytest.mark.parametrize("Name, Category, Quantity, expected", [
	("Truck", "Vehicle", "5", 1), #valid   should add
	("","empty","1", 0), #empty item name #should not add
	("empty","","1", 0), #empty category #should not add
	("The |world", "Space", "1", 0), #with | in name #should not add
	("The world", "Space|", "1", 0), #with | in category #should not add
	("The world", "Space", "-1", 0), #negative quantity #should not add
	("apple", "fruit", "1", 0), #duplicate #should not add
	("Apple", "Fruit", "50", 0), #duplicate with different case #should not add

], ids=[
	"valid","empty name", "empty category", "| in name", "| in category", 
	"negative quantity", "duplicate item", "duplicate with different case"
]


)
def test_add_item(sample_inventory, Name, Category, Quantity, expected):
	# Arrange
	expected1 = sample_inventory.copy()
	if Name == "Truck":
		expected1.append(item(name="Truck", category="Vehicle", quantity=5))
	# Act
	add_item(sample_inventory, Name, Category, Quantity)
	
	# Assert
	assert [(i.name, i.category, i.quantity) for i in sample_inventory] == [(i.name, i.category, i.quantity) for i in expected1]\


#tests number of unique items, total quantity, num of low stock, category counts, ignores capitalization
#an quantity of 5 and 4 are tested to make sure low stock counts
def test_inventory_Summary(sample_inventory, capsys):
	# Arrange
	sample_inventory.append(item(name="Truck", category="Vehicle", quantity=1))
	# Act
	inventory_summary(sample_inventory)
	output = capsys.readouterr().out
	# Assert
	assert "Unique items: 5" in output
	assert "Total quantity: 41" in output
	assert "Low stock items: 1" in output
	assert "fruit: 3" in output
	assert "tool: 1" in output
	assert "vehicle: 1" in output
	assert "Vehicle: 1" not in output

#tests empty inventory
def test_empty_inventory_summary(capsys):
	# Arrange
	empty_inventory = []
	# Act
	inventory_summary(empty_inventory)
	output = capsys.readouterr().out
	# Assert
	assert "Unique items: 0" in output
	assert "Total quantity: 0" in output
	assert "Low stock items: 0" in output
	
	