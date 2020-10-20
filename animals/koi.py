from datetime import date
from animals import Animal

class Koi(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

koi = Koi('Sesshoumaru', 'koi', 'fish flakes', 9)

print(koi.feed())