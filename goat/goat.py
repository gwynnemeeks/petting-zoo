from datetime import date

class Goat():
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

goat = Goat('Baby', 'goat', 'morning')

print(f'{goat.name} the {goat.species} is available to pet during the {goat.shift} shift.')