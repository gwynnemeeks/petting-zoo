from datetime import date
from animals import Animal

class Donkey(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift # stays on Donkey because not all animals have shifts
        self.walking = True        

donkey = Donkey('Astrix', 'donkey', 'evening', 'Mule chips', 11)

print(donkey.feed())