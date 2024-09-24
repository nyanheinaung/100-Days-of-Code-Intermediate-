import requests
import datetime

MY_LAT = 34.693737
MY_LONG = 135.502167

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # response.raise_for_status()
#
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
#
# print(iss_position)


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "Asia/Japan"
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise.split("T")[1].split(":")[0])

time_now = datetime.datetime.now()

print(sunset)
# print(time_now)
