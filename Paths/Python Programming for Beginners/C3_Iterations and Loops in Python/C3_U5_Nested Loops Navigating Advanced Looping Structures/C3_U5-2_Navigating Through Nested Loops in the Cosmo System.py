# Cosmo has 3 planets, each planet has 5 orbits. Let's explore them with nested loops:

cosmo_id = 1 
planet_limit = 4  
orbit_limit = 6

while cosmo_id < planet_limit:  
    print('Cosmo', cosmo_id)  
    orbit_id = 1  
    while orbit_id < orbit_limit:  
        print('Orbit:', orbit_id, 'of Cosmo:', cosmo_id)
        orbit_id += 1  
    cosmo_id += 1  