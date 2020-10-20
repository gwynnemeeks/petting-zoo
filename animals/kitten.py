from datetime import date
from animals import Animal

class Kitten(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift # stays on Kitten because not all animals have shifts
        self.walking = True

kitten = Kitten('Cupcake', 'kitten', 'morning', 'kitty pebbles', 55)

print(kitten.feed())