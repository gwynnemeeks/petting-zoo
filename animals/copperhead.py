from datetime import date
from animals import Animal

class Copperhead(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

copperhead = Copperhead('Wulfgang', 'copperhead', 'slither chips', 859)

print(copperhead.feed())