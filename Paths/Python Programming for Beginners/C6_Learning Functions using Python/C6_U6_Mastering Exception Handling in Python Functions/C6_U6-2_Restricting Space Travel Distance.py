def space_travel(distance):
    if distance < 0:
        raise ValueError("Distance can't be negative in space travel.")
    elif distance > 1000:
        raise ValueError("Distance can't set greater than 1000.")
    else:
        return "We are traveling {} space units.".format(distance)

def space_travel_logging(distance):
    try:
        return space_travel(distance)
    except ValueError as e:
        return "Space Travel Error: {}".format(e)

# Testing the function with a negative value
print(space_travel_logging(-100))
print(space_travel_logging(10))
print(space_travel_logging(1001))