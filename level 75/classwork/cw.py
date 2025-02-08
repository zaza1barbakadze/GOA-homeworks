class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    
    def make_sound(self, sound):
        return f"{self.name} says {sound}!"

cat = Animal("Whiskers", "Cat", 3)
print(cat.make_sound("Meow"))
