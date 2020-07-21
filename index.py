from animals import Goose
from attractions import PettingZoo


# Create a Goose
bob = Goose("Bob", "Canada goose", "watercress sandwiches")

# Create an attraction
varmint_village = PettingZoo("Varmint Village", "critters that like to dig and scurry")
varmint_village.add_animal(bob)

for animal in varmint_village.animals:
    print(animal)