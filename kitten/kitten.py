from datetime import date

class Kitten():
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

kitten = Kitten('Cupcake', 'kitten', 'morning', 'kitty pebbles')

print(kitten.feed())