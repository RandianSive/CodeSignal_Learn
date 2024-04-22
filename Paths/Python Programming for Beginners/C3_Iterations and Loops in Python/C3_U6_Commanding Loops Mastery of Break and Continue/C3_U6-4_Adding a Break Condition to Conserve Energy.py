galaxy_visibility = ['visible', 'visible', 'invisible', 'visible', 'invisible', 'visible', 'visible']

for index, status in enumerate(galaxy_visibility):
    # TODO: Write a condition to check the status of the galaxy and break the loop as required
    if status == "invisible" :
        print(f"Emergency stop at Galaxy number {index + 1} due to {status}.")
        break            
    print(f"Galaxy number {index + 1} is {status}.")
    

