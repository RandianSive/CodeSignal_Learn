def survey_universe(planets, **specs):
    print(f"Surveying {planets} planets.")
    for item, detail in specs.items():
        print(f"Detail: {item} = {detail}")

survey_universe(3, Planet1="Mars", Planet2="Venus", Planet3="Earth")