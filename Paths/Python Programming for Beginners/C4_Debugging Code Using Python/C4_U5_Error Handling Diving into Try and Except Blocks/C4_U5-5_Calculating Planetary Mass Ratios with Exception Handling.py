earth_mass = 5.97e24
celestial_body_mass = {"Mars": 6.39e23, "Jupiter": 1.898e27}


# TODO: Calculate the earth-to-mars mass ratio and handle a potential KeyError
try:
    target_body = "Mars"
    body_mass = celestial_body_mass[target_body]
    
    
    print(f"Earth-to-{target_body} mass ratio is {earth_mass/body_mass*100:.2f} %")
    
except KeyError:
    print("No such celestial in the dictionary")

