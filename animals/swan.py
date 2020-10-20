from datetime import date
from animals import Animal

class Swan(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

swan = Swan('Odette', 'swan', 'swan seeds', 456)

print(swan.feed())