from django.shortcuts import render
from django.conf import settings

# import json to load json data to python dictionary
import json

# import urllib.request to make a request to api
import urllib.request
import requests


# Create your views here.
def index(request):
    if request.method == "POST":
        city = request.POST["city"]

        # source contain JSON dat from api
        source = urllib.request.urlopen(
            "https://api.openweathermap.org/data/2.5/weather?q="
            + city
            + "&appid="
            + settings.API_KEY
        ).read()

        # converting json data to a python dictionary
        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data["sys"]["country"]),
            "coordinate": str(list_of_data["coord"]["lon"])
            + " "
            + str(list_of_data["coord"]["lat"]),
            "temp": str(list_of_data["main"]["temp"]) + "k",
            "pressure": str(list_of_data["main"]["pressure"]),
            "humidity": str(list_of_data["main"]["humidity"]),
            "feels_like": str(list_of_data["main"]["feels_like"]),
            "weather": str(list_of_data["weather"][0]["main"]),
        }
        print(data)
    else:
        data = {}

    return render(request, "main/index.html", data)


def other(request):
    if request.method == "POST":
        lat = request.POST["lat"]
        lng = request.POST["lng"]

        source = requests.get(
            "https://api.stormglass.io/v2/weather/point",
            params={
                "lat": lat,
                "lng": lng,
                "params": "waveHeight",
            },
            headers={"Authorization": settings.API_KEY2},
        )
        print(source.json())

    return render(request, "main/other.html")


# data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=london&appid=292fcebaf970199ebc95f3852f763d4c")
# data.text
# '{"coord":{"lon":-0.1257,"lat":51.5085},
# "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],
# "base":"stations","main":{"temp":280.93,"feels_like":278.36,
#                           "temp_min":279.57,"temp_max":281.62,"pressure":1008,
#                           "humidity":90},
# "visibility":10000,"wind":{"speed":4.12,"deg":200,"gust":9.77},
# "clouds":{"all":75},"dt":1701616859,
# "sys":{"type":2,"id":2075535,"country":"GB","sunrise":1701589572,"sunset":1701618868},
# "timezone":0,"id":2643743,"name":"London","cod":200}'
#
# data["coord"]
# data["wheather"]
