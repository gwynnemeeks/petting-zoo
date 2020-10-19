class SnakePit:
    
    def __init__(self, name):
        self.name = name
        self.description = "slithering scales to admire"
        self.animals = list()

    def add(self, animal):
        self.animals.append(animal)

    # def printReport(self):
    #     print(f'{self.name} is where you will find {self.description} of all sizes including')
    #     for animal in self.animals:
    #         print(f'* {animal.name} the {animal.species}')

    def __str__(self):
        attraction_animals = []
        for animal in self.animals:
            attraction_animals.append(f" * {animal.name}")
        animals_list = ('\n'.join(map(str, attraction_animals)))
        return f"{self.name} is where you'll find {self.description} like \n{animals_list}"

    @property
    def last_critter_added(self):
        return f"{self.animals[-1].name} the {self.animals[-1].species}"