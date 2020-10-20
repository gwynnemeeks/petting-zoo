from datetime import date
from .animals import Animal

class Anaconda(Animal):
    def __init__(self, name, species, food):
        self.slithering = True

anaconda = Anaconda('Nicki', 'anaconda', 'slither chips')

print(anaconda)