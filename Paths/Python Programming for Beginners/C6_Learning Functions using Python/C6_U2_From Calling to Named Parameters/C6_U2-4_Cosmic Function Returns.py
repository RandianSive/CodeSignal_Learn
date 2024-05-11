def inspect_cosmic_payload(fuel, food):
    # TODO: Return the fuel and food status messages using f-strings
    # Output example: "Payload fuel level: {fuel}", "Payload food stock: {food}"
    return f"Payload fuel level: {fuel}", f"Payload food stock: {food}"

# Unpacking multiple return values using named parameters
fuel_status, food_status = inspect_cosmic_payload(fuel="Full", food="Empty")  # TODO: Call the function with the correct named parameters

print(fuel_status)
print(food_status)