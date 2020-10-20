from datetime import date
from animals import Animal

class Dog(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift # stays on Dog because not all animals have shifts
        self.walking = True

dog = Dog('Zoey', 'dog', 'afternoon','puppy snacks', 0)

print(dog.feed())