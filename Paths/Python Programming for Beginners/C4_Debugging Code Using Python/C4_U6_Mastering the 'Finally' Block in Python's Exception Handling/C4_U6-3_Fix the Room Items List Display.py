room_items = ['table', 'chair', 'lamp', 'sofa', 'cushions']

try:
    room_items.remove('bed')
except ValueError:
    print("Cannot remove 'bed' as it is not in the list.")
finally:
    print("The current list of items are:")
    for item in room_items:
        print(item)