astronomy_objects_data = [
    ["stars", ["visible", "visible", "invisible"]],
    ["planets", ["visible", "invisible", "invisible"]],
    ["galaxies", ["invisible", "visible", "visible"]],
    ["comets", ["visible", "invisible", "visible"]],
]

for astro_object in astronomy_objects_data:
    object_type, visibility = astro_object
    print('Exploring object:', object_type)
    for status in visibility:
        if status == "invisible":
            print("Invisible object detected, we should leave the object immediately!")
            break
        print('Visibility:', status)