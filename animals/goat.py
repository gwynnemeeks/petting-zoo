from datetime import date
from animals import Animal

class Goat(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift # stays on Goat because not all animals have shifts
        self.walking = True

goat = Goat('Baby', 'goat', 'morning', 'goat snacks', 75)

print(goat.feed())