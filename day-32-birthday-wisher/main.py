##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import smtplib
import random
import pandas

byear = 2020
bmonth = 9
bday = 25

today = dt.datetime(year=byear, month=bmonth, day=bday)

def wish_birthday(name, email):

    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as base_letter:
        birthday_message = base_letter.read()
        birthday_message = birthday_message.replace("[NAME]", name)

    my_email = "testforlearning12@gmail.com"
    my_password = "ynlztdsarwvxmhyd"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email,
                            msg=f"Subject:Happy Birthday!!\n\n{birthday_message}"
                            )

def check_birthday():
    bd_data = pandas.read_csv("birthdays.csv")
    for bd in bd_data.iterrows():
        if bd[1]["month"] == today.month and bd[1]["day"] == today.day:
            wish_birthday(bd[1]["name"], bd[1]["email"])


check_birthday()
