from datetime import date
from animals import Animal

class Python(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

python = Python('John', 'python', 'cleese', 69)

print(python.feed())