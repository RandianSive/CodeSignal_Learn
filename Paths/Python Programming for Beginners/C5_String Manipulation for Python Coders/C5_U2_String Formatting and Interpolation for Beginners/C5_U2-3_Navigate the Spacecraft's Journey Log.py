day = 5
planet_from = "Mercury"
planet_to = "Earth"
distance_covered = 77.3 # in million kilometers
time_taken = 2.9 # in days
speed = round(distance_covered / time_taken, 2)

log_message = "Day {}: Left {}, heading to {}. Covered a distance of {} million kilometers in {} days. Average speed: {} million kilometers/day.".format(day, planet_from, planet_to, distance_covered, time_taken, speed)
print(log_message)