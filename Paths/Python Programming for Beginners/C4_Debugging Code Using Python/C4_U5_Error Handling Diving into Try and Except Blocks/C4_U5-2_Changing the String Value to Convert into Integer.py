try:
    stars_in_galaxy = "Cosmo"
    numerical_stars = int(stars_in_galaxy)
except ValueError:
    print("Hmmm, seems like you tried converting a non-numeric value to an integer!")