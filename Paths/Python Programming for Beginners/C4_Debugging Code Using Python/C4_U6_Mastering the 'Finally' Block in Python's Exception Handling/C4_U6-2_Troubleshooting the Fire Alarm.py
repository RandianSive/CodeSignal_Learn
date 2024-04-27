office_equipment = ['computers', 'printers', 'coffee machine']
element = "scanner"

try:
    office_equipment.remove(element)
except ValueError:
    print("{} is not found in office equipment list.".format(element))
finally:
    print("Regardless, please remember to clean up after work.")