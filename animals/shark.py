from datetime import date
from animals import Animal

class Shark(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

shark = Shark('Kaiju', 'shark', 'chum', 99)

print(shark.feed())