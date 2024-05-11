def travel_to_galaxy(galaxy, *spaceships, captain="Captain Kirk", **crew_members):
    print(f"{captain} is leading the voyage to {galaxy} with:")
    for ship in spaceships:
        print(f" - {ship}")

    print("\nThe crew members include:")
    for position, member in crew_members.items():
        print(f"{position}: {member}")

travel_to_galaxy("Andromeda", "Enterprise", "Discovery", captain="Cosmo", Pilot="Spock", Engineer="Scott")