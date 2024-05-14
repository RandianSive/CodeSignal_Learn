class Asteroid:
    def __init__(self, name, composition):
        self.name = name
        self.composition = composition

bennu = Asteroid("Bennu", "Carbonaceous")
print(bennu.name) # Supposed to print: "Bennu"
print(bennu.composition) # Supposed to print: "Carbonaceous"