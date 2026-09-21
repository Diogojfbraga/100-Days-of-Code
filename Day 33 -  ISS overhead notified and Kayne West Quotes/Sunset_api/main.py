import requests
from datetime import datetime

MY_LAT = 53.480709
MY_LONG = -2.234380


paramenters = {
    "lat": MY_LAT,
    "long": MY_LONG
}

response = requests.get(url=f'https://api.sunrise-sunset.org/v2?lat={paramenters["lat"]}&lng={paramenters["long"]}')
response.raise_for_status()

data = response.json()

# print(data)
sunrise = data["sunrise"]


if paramenters["lat"] == data["lat"] and paramenters["long"] == data["lng"]:
    txt = sunrise
    date = txt.split("T")
    time = txt.split("+")

  
    date = date[0]
    time = time[1]

print(date, time)




# print(lat)