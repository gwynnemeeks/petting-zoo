from datetime import date
from animals import Animal

class Anaconda(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

anaconda = Anaconda('Nicki', 'anaconda', 'slither chips', 546)

print(anaconda.feed())