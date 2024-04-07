# Our goal is to find unique colors across two different baskets of fruits
basket_1 = {"apple": "Red", "banana": "Yellow", "grape": "Purple", "pear": "Green"}
basket_2 = {"kiwi": "Brown", "mango": "Orange", "banana": "Yellow", "apple": "Green"}

# Let's create sets of colors from each basket
colors_1 = set(basket_1.values())
colors_2 = set(basket_2.values())

unique_colors = colors_1 | colors_2
print("Unique fruit colors across both baskets:", unique_colors)