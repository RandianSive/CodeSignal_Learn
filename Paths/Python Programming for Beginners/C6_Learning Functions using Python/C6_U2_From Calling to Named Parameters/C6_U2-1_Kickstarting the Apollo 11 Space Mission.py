def initialize_spacecraft(mission_name, start_date, command_center):
    return mission_name + " initiated", "Mission start date: " + start_date, "Command Center: " + command_center

mission_name, start_date, command_center = initialize_spacecraft(mission_name="Apollo 11", start_date="16th July 1969", command_center="Houston")

print(mission_name)  # Prints: "Apollo 11 initiated"
print(start_date)  # Prints: "Mission start date: 16th July 1969"
print(command_center)  # Prints: "Command Center: Houston"