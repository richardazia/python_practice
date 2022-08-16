from sre_constants import JUMP


class cat: 

    sub_species = 'Felinae'
    binomial_name = 'Felis catus'
    herd_of_cats = 0

    def __init__(self, name, breed, location):
        self.name = name
        self.breed = breed
        self.location = location
        self.toys = []
        cat.herd_of_cats += 1

    @classmethod
    def register_stray(cls):
        return cls('TBD', 'TBD', 'TBD')

    def purr(self):
        print(f"{self.name} just started to purr. {self.name} is happy.")

    def pipe(self):
        print("Stare and listen to pipe noises")
    
    def jump():
        print("A cat just pounced")

    def play_with_toy(self, new_toy): 
        if new_toy not in self.toys:
            self.toys.append(new_toy)
    
    def name_plays_with_toy(self, new_toy):
        if new_toy in self.toys:
            print(f"{self.name} is playing {new_toy}")
        else:
            print(f"{self.name} does not have {new_toy}")

balanced = cat("Balanced", "siamese", "St George")
sprinter = cat("Sprinter", "manx", "Leukerbad")
navigator = cat("Navigator", "mongrel", "Morges")

print(f"Subspecies: {balanced.sub_species}")
print(type(balanced))
print(isinstance(balanced, cat))
balanced.purr()
sprinter.purr()
print(balanced.sub_species)
print(sprinter.binomial_name)
print(navigator.binomial_name)

found_cat = cat.register_stray()

print(found_cat.breed)

cat.jump()
cat.jump()
cat.jump()
cat.jump()

balanced.play_with_toy('Jump onto cupboard door')
balanced.play_with_toy('Chase the red dot')
balanced.play_with_toy('Catch a lizard')
balanced.play_with_toy('with a duck')

print(balanced.toys)

balanced.name_plays_with_toy("with a duck")
balanced.name_plays_with_toy("Catch a lizard")
balanced.name_plays_with_toy("Chase the red dot")
print(cat.herd_of_cats)

# Using Super
