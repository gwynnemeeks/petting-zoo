from datetime import date
from animals import Animal

class Llama(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift # stays on Llama because not all animals have shifts
        self.walking = True

llama = Llama('Henrietta', 'llama', 'afternoon', 'apples, maybe?', 88)

print(llama.feed())