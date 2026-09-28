class item:

    def __init__(self,name, category,quantity):
        self.name = name
        self.category = category
        self.quantity = quantity
    def __str__(self):
        return f"{self.name}, {self.category}, {self.quantity}"

inventory = [
  #  item("screwdriver","tool", 1), 
  #  item("hammer","tool", 2)
    ]


