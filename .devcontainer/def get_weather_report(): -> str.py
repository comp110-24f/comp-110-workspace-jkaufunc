def get_weather_report() -> str:
    weather: str = input("What is the weather?")
    if (weather == "rainy") or (weather == "cold"):
        print("bring a jacket!")
    elif weather == "hot":
        print("keep cool out there!")
    else:
        print("I don't recognize that weather.")
    return weather


def weather_report() -> None:
    weather = input("What is the weather?")
    if (weather == "rainy") or (weather == "cold"):
        print("You'd better grab a jacket!")
    elif weather == "hot":
        print("Stay cool out there!")
    else:
        print("I don't know what kind of weather that is???")
