from datetime import date

class Swan():
    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food
        self.__chip_number = chip_num

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

    @property # the getter
    def chip_number(self):
        return self.__chip_number

    @chip_number.setter #the setter
    def chip_number(self, number):
        pass

swan = Swan('Odette', 'swan', 'swan seeds', 456)

print(swan.chip_number)