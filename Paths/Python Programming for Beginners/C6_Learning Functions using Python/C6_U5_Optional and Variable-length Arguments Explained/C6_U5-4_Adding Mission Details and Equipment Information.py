def space_mission_report(name, mission="Unspecified", *details, **equipment):
    print(f"Astronaut {name} is prepared for the mission: {mission}")
    
    print("Mission Details:")
    # TODO: Add code to print each detail of the mission
    for mission_detail in details:
        print(f"- {mission_detail}")
    
    print("Equipment details are as follows:")
    # TODO: Add code to print the equipment details 
    for catalog,spec in equipment.items():
        print(f"{catalog}: {spec}")

space_mission_report("John Doe", "Mars Rover Deployment", "Exploration", "Research", Spacesuit="Advanced", Food="Boost Pack", Communication="Satellite Radio")