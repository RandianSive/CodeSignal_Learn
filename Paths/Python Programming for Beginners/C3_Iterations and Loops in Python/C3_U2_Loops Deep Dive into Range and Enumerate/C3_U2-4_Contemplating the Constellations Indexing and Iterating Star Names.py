stars = ["Sun", "Polaris", "Betelgeuse", "Sirius", "Vega"]

# TODO: Enumerate over the stars list and print each star with its index
for index, star in enumerate(stars):
    # Star indices should start with 1: 1, 2, 3, ...
    print("Star", index + 1 , "in my list is", star)

# TODO: Use the range function to iterate over the stars list **in reverse order**
# and print each star with its index
for i in range(len(stars)-1, -1, -1):
    # Star indices should start with 1: len(stars), len(stars) - 1, ..., 1
    print("Star", i + 1, "in my list is", stars[i])