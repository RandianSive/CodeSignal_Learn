def rocket_speed_check(speed):
    if speed < 0:
        raise ValueError("Speed can't be negative!")
    else:
        print(f"Speed {speed} check ok!")

def launch_rocket():
    # TODO: Call the `rocket_speed_check` function and do exception handling
    # Log the error to the console if it appears
    try:
        rocket_speed_check(-1)
        
    except ValueError as err_msg:
        print("Speed alert! Error:", err_msg)

launch_rocket()