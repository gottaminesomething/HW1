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