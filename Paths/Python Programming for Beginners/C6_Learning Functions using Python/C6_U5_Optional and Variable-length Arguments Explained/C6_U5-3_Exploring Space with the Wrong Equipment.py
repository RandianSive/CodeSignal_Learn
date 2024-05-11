def planets(*planets_name, orbit="None", **characteristics):
    print("Planets in our Space Mission:")
    
    for planet in planets_name:
        print(f"- {planet}")
        
    print(f"All planets are in {orbit} orbit.")
    
    for key, value in characteristics.items():
        print(f"{key}: {value}")

planets("Mars", "Jupiter", "Saturn", orbit="Elliptical", Color="Red", Radius=6792)