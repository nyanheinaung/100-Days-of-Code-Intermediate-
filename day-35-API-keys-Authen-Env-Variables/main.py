import requests

api_key = "14a9183a2be8704af5163d6ce6a16588"
LATITUDE = 34.710722
LONGITUDE = 135.529917

parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": api_key
}


response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

num = 1
weather_id = response.json()["list"][num]["weather"][0]["id"]
weather_description = response.json()["list"][num]["weather"][0]["description"]
print(weather_id, weather_description)

