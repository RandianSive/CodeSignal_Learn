# Dictionary of space suits and their weights in kg
space_suit_weights = {'Mercury suit': 21, 'Gemini suit': 16, 'Apollo suit': 32, 'Space Shuttle suit': 50}

total_weight = 0
# TODO: Use a For Loop to calculate the total weight of all space suits
for suit_weight in space_suit_weights.values():
    total_weight += suit_weight

print('Total suits weight:', total_weight)