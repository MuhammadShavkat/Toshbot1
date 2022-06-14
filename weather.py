import requests as requests
from config import open_w_token
import requests
#from pprint import pprint


def get_weather(city):
    try:
        result = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_w_token}&units=metric")

        data = result.json()
        shahar = data["name"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        speed = data["wind"]["speed"]
        deg = data["wind"]["deg"]
        return (f"Shahar nomi:{shahar}\n"
            f"temperatura:{temp}\n"
            f"namlik:{humidity}%\n"
            f"shamol tezligi:{speed}m/s\n"
            f"shamol darajasi:{deg}\n")

    except Exception as ex:
        print(ex)
        print("xatolik")
# def main():
#    city = input("shahar nomi kirit:")
#    get_weather(city,open_w_token)
#    print(city)

# main()
