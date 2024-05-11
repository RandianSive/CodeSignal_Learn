# A list of star temperatures in thousands of Kelvin
star_temps = [5778, 9941, 3700, 25340, 7220]

# Let's find the coldest and hottest stars
coldest_star = min(star_temps)
hottest_star = max(star_temps)

# Let's also find the average temperature of the stars.
average_temp = round(sum(star_temps)/len(star_temps))

print("Coldest Star:", coldest_star, "K")
print("Hottest Star:", hottest_star, "K")
print("Average Star Temperature:", average_temp, "K")