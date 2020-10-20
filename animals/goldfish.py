from datetime import date
from animals import Animal

class Goldfish(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

goldfish = Goldfish('Goldie', 'goldfish', 'fish flakes', 2)

print(goldfish.feed())