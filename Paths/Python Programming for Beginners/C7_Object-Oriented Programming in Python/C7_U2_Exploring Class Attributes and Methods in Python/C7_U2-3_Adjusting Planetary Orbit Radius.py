class Cosmos:
    planet = 8
    orbit = 108.2 
    
    def explore(self):
        return f"Exploring a cosmos with {self.planet} planets, each with an orbit of {self.orbit} million km"

cosmos = Cosmos()
print(cosmos.explore())