# TODO: Define a function to calculate the mass of a planet given its diameter and density.
# Remember, the density and diameter should be positive.
# Formula: mass = (4/3) * 3.14 * (diameter / 2)**3 * density

def calcu_value(diameter,density):
    if diameter <= 0 or density <= 0:
        raise ValueError("Diameter and density of planet can't be zero or negative!")
    else:
        return (4/3) * 3.14 * (diameter / 2)**3 * density


def planet_mass(diameter,density):
    try:
        result = calcu_value(diameter,density)
        print(f"The mass of the planet is {result:.2f}")
    except ValueError as err_msg:
        print(f"Calculate error: {err_msg}")

# To call the above function and print the result. 
# Also, make sure to handle the exceptions and print the error from the exception if there's any. 

planet_mass(2,2)

planet_mass(2,-1)