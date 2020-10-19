from anaconda import Anaconda
from cottonmouth import Cottonmouth
from copperhead import Copperhead
from datetime import date
from dog import Dog
from donkey import Donkey
from goat import Goat
from goldfish import Goldfish
from kingsnake import Kingsnake
from kitten import Kitten
from koi import Koi
from llama import Llama
from goldfish import Goldfish
from mallard import Mallard
from python import Python
from shark import Shark
from swan import Swan
from attractions import PettingZoo, SnakePit, Wetlands

varmint_village = PettingZoo("Varmint Village")
slither_inn = SnakePit("Slither Inn")
fish_pond = Wetlands("Fish Pond")

anaconda = Anaconda('Nicki', 'anaconda', 'slither chips')
copperhead = Copperhead('Wulfgang', 'copperhead', 'slither chips')
cottonmouth = Cottonmouth('Emelda', 'cottonmouth', 'mice')
dog = Dog('Zoey', 'dog', 'afternoon','puppy snacks')
donkey = Donkey('Astrix', 'donkey', 'evening', 'Mule chips')
goat = Goat('Baby', 'goat', 'morning', 'goat snacks')
goldfish = Goldfish('Goldie', 'goldfish', 'fish flakes')
kingsnake = Kingsnake('Youngdo', 'kingsnake', 'mice')
kitten = Kitten('Cupcake', 'kitten', 'morning', 'kitty pebbles')
koi = Koi('Sesshoumaru', 'koi', 'fish flakes')
llama = Llama('Henrietta', 'llama', 'afternoon', 'apples, maybe?')
mallard = Mallard('Minnie', 'mallard', 'duck seed')
python = Python('John', 'python', 'rats')
shark = Shark('Kaiju', 'shark', 'chum')
swan = Swan('Odette', 'swan', 'swan seeds', 456)

varmint_village.add(dog)
varmint_village.add(donkey)
varmint_village.add(goat)
varmint_village.add(kitten)
varmint_village.add(llama)
slither_inn.add(anaconda)
slither_inn.add(copperhead)
slither_inn.add(cottonmouth)
slither_inn.add(kingsnake)
slither_inn.add(python)
fish_pond.add(goldfish)
fish_pond.add(koi)
fish_pond.add(mallard)
fish_pond.add(shark)
fish_pond.add(swan)

print(swan.chip_number)

print(varmint_village.last_critter_added)
print(slither_inn.last_critter_added)
print(fish_pond.last_critter_added)