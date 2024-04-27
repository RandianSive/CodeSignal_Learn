try:
    celestial_body_mass = {"Earth": 5.97e24, "Moon": 7.35e22}
    
    # TODO: Retrieve the mass of Jupiter from our dictionary and handle any KeyError exception that arises.
    print(celestial_body_mass["Jupiter"])

except KeyError:
    print("Error: The mass of the specified celestial body is not available in the dictionary.")