import requests
from twilio.rest import Client

account_sid = "" # Use "Twilio" account sid here
auth_token = "" # Use "Twilio" auth_token here
api_key = "" # Use "Openweather" api key here
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
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain. You'd better bring an ☂️!",
        from_="+12093085412",
        to="+818041584210"
    )
    print(message.status)

