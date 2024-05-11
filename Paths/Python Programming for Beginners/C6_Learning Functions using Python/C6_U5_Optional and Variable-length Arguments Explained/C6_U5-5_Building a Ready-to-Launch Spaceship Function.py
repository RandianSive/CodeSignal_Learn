# TODO: Define a function named 'spaceship_params' which accepts arguments:
# pilot's name, names of crew members, optional spaceship name, and other optional spaceship specifications.

def spaceship_params(pilot_name,*crew_name,spaceship_name= "Explorer", **spaceship_spec):
    

# TODO: Within the function, print the pilot's name and the names of the crew members. 
# Also print the name of the spaceship and its specifications.
    print(f"Spaceship pilot: {pilot_name}")
    print("Crew:")
    for crew in crew_name:
        print(f"- {crew}")
    
    print()
    
    print(f"Spaceship named {spaceship_name} and its spec:")
    for catalog,spec in spaceship_spec.items():
        print(f"{catalog}: {spec}")

# TODO: Call the above function with suitable arguments to test if it's working as expected.
spaceship_params("Cosmo","Starlord","Darth Vadar", "Luke", spaceship_name= "Voyager", Storage = "100000L", Fuel = "X-105")