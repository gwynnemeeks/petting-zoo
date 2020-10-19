from datetime import date

class Copperhead():
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

copperhead = Copperhead('Wulfgang', 'copperhead', 'slither chips')

print(copperhead.feed())