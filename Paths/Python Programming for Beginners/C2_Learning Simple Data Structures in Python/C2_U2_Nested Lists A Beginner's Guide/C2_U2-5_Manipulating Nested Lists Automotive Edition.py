# Nested list of car brands and models
cars = [['Tesla', 'Model 3'], ['Ford', 'Mustang'], ['BMW', 'X5']]

# TODO: Append a new brand and model to the main list
cars.append(['Toyota', 'Yaris'])
# TODO: Remove 'Mustang' from the Ford sublist
cars[1].remove('Mustang')
# TODO: Add 'F150' to the Ford sublist
cars[1].append('F150')
# TODO: Print the updated car list
print(cars)