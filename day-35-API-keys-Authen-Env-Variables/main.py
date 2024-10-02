import requests

api_key = "14a9183a2be8704af5163d6ce6a16588"
LATITUDE = 34.710722
LONGITUDE = 135.529917

parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": api_key,
    "cnt": 4,
}


response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()["list"]

need_umbrella = False
for hour_data in weather_data:
    weather_id = hour_data["weather"][0]["id"]
    print(weather_id)
    if weather_id < 700:
        need_umbrella = True

if need_umbrella:
    print("Bring an umbrella!")

