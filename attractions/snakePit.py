class SnakePit:
    
    def __init__(self, name):
        self.name = name
        self.description = "slithering scales to admire"
        self.animals = list()

    def add(self, animal):
        self.animals.append(animal)

    def printReport(self):
        print(f'{self.name} is where you will find {self.description} of all sizes including')
        for animal in self.animals:
            print(f'* {animal.name} the {animal.species}')