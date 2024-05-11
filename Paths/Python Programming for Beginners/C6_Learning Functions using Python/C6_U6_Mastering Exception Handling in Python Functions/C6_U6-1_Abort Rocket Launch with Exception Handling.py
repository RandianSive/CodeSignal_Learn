def calculate_trajectory(speed, time):
    if time <= 0:
        raise ValueError("Time can't be zero or negative.")
    else:
        return speed * time

def launch_rocket():
    try:
        print(calculate_trajectory(5000, 0))
    except ValueError as e:
        print("Abort launch! Error:", e)
        
launch_rocket()