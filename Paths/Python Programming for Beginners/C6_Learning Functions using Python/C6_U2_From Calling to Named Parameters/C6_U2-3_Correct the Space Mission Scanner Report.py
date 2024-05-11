def scan_planet(planet, system):
    print('Scanning planet', planet, 'in', system)

def space_mission():
    print('Mission start.')
    scan_planet(planet='Mars', system = 'Solar System')
    scan_planet(planet='Earth', system =  'Solar System')

space_mission()