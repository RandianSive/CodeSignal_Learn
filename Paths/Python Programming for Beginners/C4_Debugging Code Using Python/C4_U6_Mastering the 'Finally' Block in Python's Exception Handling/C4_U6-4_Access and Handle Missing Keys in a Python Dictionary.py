# Office setting
office_equipment = {'computers': 5, 'coffee machine':3 ,'scanner': 2}

try:
    #TODO: Write a line to access an item in the dictionary, which will throw the KeyError exception.
    require_item = office_equipment['printer']
except KeyError:
    print("Can't find 'printer' in the office equipment.")
# TODO: implement a 'finally' block to print the current state of the office equipment dictionary
finally:
    print("Current office equipment:")
    for equipment in office_equipment:
        print(equipment)