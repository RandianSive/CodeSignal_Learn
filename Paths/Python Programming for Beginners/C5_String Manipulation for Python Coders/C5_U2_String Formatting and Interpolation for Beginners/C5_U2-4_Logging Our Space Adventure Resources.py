day = 20
planet = "Saturn"
log_part1 = "Day %d: Arrived at %s. " % (day, planet)

fuel = "75%"
water = "50%"
food = "70%"
# TODO: Write a log message about the current resources using f-string interpolation
log_part2 = f"Resource stats: Fuel: {fuel}, Water: {water}, Food: {food}."

log = log_part1 + log_part2
print(log)