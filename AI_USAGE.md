| What I asked about | AI assistance received | Policy category |
|---|---|---|
| Objects vs. dictionaries and list indexing | Explained differences between objects and dictionaries and how Python list indexing works | Explain programming concepts |
| Printing an object produced `<__main__.item object at ...>` | Explained why Python displayed the object that way and how object attributes can be accessed | Explain programming concepts / Diagnose errors |
| Learning OOP through the inventory project | Explained how classes, objects, attributes, and `self` relate to the inventory implementation | Explain programming concepts |
| Cloning the project onto another computer | Provided `git clone` syntax and explained how cloning works | Explain programming concepts / Suggest possible code |
| Persistently storing objects in a text file | Explained serialization and suggested storing object attributes in a text format such as `Name|Category|Quantity` | Explain programming concepts / Suggest possible code |
| Designing the `Name|Category|Quantity` format | Explained that text-file values are strings when loaded and that quantity would need conversion back to an integer | Explain programming concepts |
| Using `f.write()` | Explained `f.write()`, string concatenation, integer-to-string conversion, and writing newlines | Explain programming concepts / Suggest possible code |
| Save function was not writing correctly | Diagnosed issues involving iteration, file opening, and string/integer concatenation | Diagnose errors |
| Using `for x in io.inventory` | Explained that `x` represents the object itself rather than an index and how its attributes can be accessed | Explain programming concepts / Diagnose errors |
| Save function still appeared not to write | Helped debug whether the save function and file-writing code were executing | Diagnose errors |
| Missing `()` on `save_list_items()` | Explained the difference between referencing a function and calling a function | Diagnose errors / Explain programming concepts |
| Reviewing the working save loop | Reviewed why iterating through inventory objects and writing their attributes worked | Review code / Explain programming concepts |
| Parsing `|` separated text | Suggested Python's `.split("|")` method and explained how the resulting values could be accessed | Explain programming concepts / Suggest possible code |
| `IndexError` while loading inventory | Diagnosed that the program was iterating through and modifying the inventory simultaneously and suggested iterating through file lines instead | Diagnose errors / Suggest possible code |
| Items duplicated after loading and saving | Diagnosed that items already existed in memory before saved items were loaded, causing duplicates when everything was saved again | Diagnose errors / Suggest refactoring |
| AI use policy and Codex-generated menu | Reviewed the provided AI policy and explained how the generated testing menu fit the permitted uses | Review / documentation assistance |
| Used Codex to generate a simple command-line menu for testing item creation, saving, and printing during program execution. I reviewed and tested the generated menu before integrating it.
| Used chatgpt to give me a hint on how to get counts of each category without giving me any code | advice that i should use a dictionary to store the information  | Explain programming concepts

# **homework 2**

| What I asked about | AI assistance received | Policy category |
|---|---|---|
| used Codex to change functions in `main.py` from using `io.inventory` to using a paramater called `inventory` | Refactoring simplification | how AI assisted with testing or refactoring.
**prompt**
in main.py kindly refactor every instance of io.inventory inside a function such as:
    def save_list_items():
    with open(inventoryFile, "w") as f:
        for x in io.inventory:
            f.write(x.name + "|" + x.category + "|" + str(x.quantity) + "\n")

into being parameter form
    
    def save_list_items(inventory):
    ...

as well as updating the function calls in menu() to not leave any errors from the refactoring.
ignore test_inventory_manager.py from any edits. do not go above and beyond and change things i did not ask you to change

| What I asked about | AI assistance received | Policy category | prompt|
|---|---|---|---|
| used codex to automatically convert my search tests to be parametrized after i did it myself for the first couple - previous version uncommitted| simplification of repeated task | how AI assisted with testing or refactoring | "for the rest of my search tests, parametrize them similar to test_search_exact_item() and test_search_partial()"
|used codex to automatically convert my inventory = [...] into inventory = sample_inventory after i created the fixture myself | simplification of repeated task | how AI assisted with testing or refactoring | "in test_inventory_manager.py replace any inventory = [...] with the fixture sample_inventory. leave any inventory = [...] that are specialized per the test but any that are repeated can be replaced"

proof of paramterizing being automated
        ## Pytest Results

**Environment:** Python 3.12.3 | pytest 9.2.0

### Before Automation — 13 Tests

```bash
test_load_inventory_manager_and_as_int      PASSED [  7%]
test_empty_load_list_items                  PASSED [ 15%]
test_load_list_items_EmptyLine               PASSED [ 23%]
test_save_multiple_items                     PASSED [ 30%]
test_save_empty_inventory                    PASSED [ 38%]
test_save_then_load_inventory                PASSED [ 46%]
test_seach_exact_item[1-apple-apple]         PASSED [ 53%]
test_seach_exact_item[2-tool-tool]           PASSED [ 61%]
test_seach_exact_item[3-10-10]               PASSED [ 69%]
test_search_partial                          PASSED [ 76%]
test_search_duplicates                       PASSED [ 84%]
test_search_no_matching_and_fuzzy            PASSED [ 92%]
test_search_with_whitespace                  PASSED [100%]

13 passed in 0.05s
```

### After Automation — 23 Tests

```bash
test_load_inventory_manager_and_as_int      PASSED [  4%]
test_empty_load_list_items                  PASSED [  8%]
test_load_list_items_EmptyLine               PASSED [ 13%]
test_save_multiple_items                     PASSED [ 17%]
test_save_empty_inventory                    PASSED [ 21%]
test_save_then_load_inventory                PASSED [ 26%]
test_seach_exact_item[1-apple-apple]         PASSED [ 30%]
test_seach_exact_item[2-tool-tool]           PASSED [ 34%]
test_seach_exact_item[3-10-10]               PASSED [ 39%]
test_search_partial[1-app-apple]             PASSED [ 43%]
test_search_partial[2-to-tool]               PASSED [ 47%]
test_search_partial[3-100-10]                PASSED [ 52%]
test_search_partial[3-1-10]                  PASSED [ 56%]
test_search_duplicates[1-apple-expected0]   PASSED [ 60%]
test_search_duplicates[2-fruit-expected1]   PASSED [ 65%]
test_search_duplicates[3-10-expected2]      PASSED [ 69%]
test_search_no_matching_and_fuzzy[1-Spaceship-expected0] PASSED [ 73%]
test_search_no_matching_and_fuzzy[1-grape-expected1]     PASSED [ 78%]
test_search_no_matching_and_fuzzy[2-food-expected2]      PASSED [ 82%]
test_search_no_matching_and_fuzzy[3-8-expected3]         PASSED [ 86%]
test_search_with_whitespace[1--expected0]    PASSED [ 91%]
test_search_with_whitespace[2--expected1]    PASSED [ 95%]
test_search_with_whitespace[3--expected2]    PASSED [100%]

23 passed
```