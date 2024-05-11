def check_planet(planet):
    if planet not in ['Earth', 'Mars', 'Mercury', 'Venus', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']:
        raise ValueError(f"{planet} is not in our solar system!")

def journey_to_planet(planet):
    try:
        check_planet(planet)
        print(f"On the way to {planet}!")
    except TypeError:
        print("Please enter a valid planet!")
    except ValueError as err_msg:
        print(err_msg)

journey_to_planet('Pluto')