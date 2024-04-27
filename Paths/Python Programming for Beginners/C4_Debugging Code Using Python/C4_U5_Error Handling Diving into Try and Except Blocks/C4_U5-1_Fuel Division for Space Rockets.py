try:
    fuel = 100
    rockets = 0
    fuel_per_rocket = fuel / rockets
except ZeroDivisionError:
    print("Oops! Number of rockets can't be zero!")