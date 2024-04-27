try:
    distance_to_moon = 384400
    rocket_speed = 100
    travel_time_to_moon = distance_to_moon / rocket_speed
    print("Travel time to moon: ", travel_time_to_moon, " hours")  
except ZeroDivisionError:
    print("Oops! Cannot calculate travel time with zero speed.")