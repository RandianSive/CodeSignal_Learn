constellation_data = [
    ["scutum", ["visible", "visible", "not visible"]],
    ["cassiopeia", ["visible", "visible", "visible"]],
    ["orion", ["not visible", "not visible", "visible"]],
    ["cygnus", ["visible", "not visible", "visible"]]
]

for constellation in constellation_data:
    name, visibility = constellation
    if name =="orion":
        print("Skip Orion")
        continue
    print('Constellation:', name)
    for status in visibility:
        print('Visibility:', status)