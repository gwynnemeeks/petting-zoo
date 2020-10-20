from datetime import date
from animals import Animal

class Mallard(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

mallard = Mallard('Minnie', 'mallard', 'duck seed', 400)

print(mallard.feed())