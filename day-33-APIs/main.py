import requests
import datetime
import smtplib
import time

MY_LAT = 34.693737
MY_LONG = 135.502167


def iss_is_near_me():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    return -5 < iss_latitude - MY_LAT < 5 and -5 < iss_longitude - MY_LONG < 5


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": "Japan"
    }

    sunset_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    sunset_response.raise_for_status()

    data = sunset_response.json()

    sunset = data["results"]["sunset"]
    sunrise = data["results"]["sunrise"]
    sunset_hour = int(sunset.split("T")[1].split(":")[0])
    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])

    time_now = datetime.datetime.now().hour

    return time_now > sunset_hour or time_now < sunrise_hour


def send_iss_noti_email():
    my_mail = "testforlearning12@gmail.com"
    password = "ynlztdsarwvxmhyd"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs="waiphyophyonyein@gmail.com",
            msg=f"Subject:ISS is near you!!\n\n"
                f"Hey the international space station is near you. "
                f"You should look up at the sky. "
                f"There is a high chance you will spot it!"
        )


while True:
    time.sleep(60)
    if iss_is_near_me() and is_night():
        send_iss_noti_email()
