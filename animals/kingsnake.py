from datetime import date
from animals import Animal

class Kingsnake(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

kingsnake = Kingsnake('Youngdo', 'kingsnake', 'mice', 38)

print(kingsnake.feed())