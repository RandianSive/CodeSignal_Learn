# Defining an array with some celestial bodies and their observed status
celestial_bodies = [('Star 1', "observed"), ('Star 2', "unobserved"), ('Star 3', "observed"), ('Star 4', "unobserved")]

# TODO: Iterate over each celestial body in "celestial_bodies"
for star,status in celestial_bodies:
    # TODO: print a message saying that we are observing the current celestial body
    print(f"Observing {star}...")
    # TODO: add a condition that checks if the current celestial body is unobserved
    # If the body is unobserved, print a warning message
    # and skip to the next iteration of the loop
    if status == "unobserved":
        print(f"Warning! Unobserved celestial body {star},leaving to the next celestial body now.\n")
        continue
    # TODO: print a message saying the current celestial body and its observed status
    print(f"{star} is {status}.\n")