import smtplib
import datetime as dt
import random

QUOTE_DAY = 5


def send_motivation_mail():
    with open("quotes.txt") as quotes_data:
        quotes = quotes_data.readlines()
        quote_for_today = random.choice(quotes)

    my_email = "testforlearning12@gmail.com"
    password = "ynlztdsarwvxmhyd"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="testforlearning12@yahoo.com",
                            msg=f"Subject:Monday Motivational Quote\n\n{quote_for_today}")


today = dt.datetime.now().weekday()
if today == QUOTE_DAY:
    send_motivation_mail()


# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# day_of_week = now.weekday()
# if year == 2024:
#     print(day_of_week)
#
# date_of_birth = dt.datetime(year=1993, month=1, day=1)
# print(date_of_birth)



# MyEmail = "xxxyyyzzz@gmail.com"
# MyPassword = "This shall be the app password!"
# with smtplib.SMTP("smtp.gmail.com", 587) as MyConnection:
#     MyConnection.starttls()
#     MyConnection.login(user=MyEmail, password=MyPassword)
#     MyConnection.sendmail(from_addr=MyEmail,
#                           to_addrs="aaabbbccc@gmail.com",
#                           msg=f"Subject:some subject \n\ntestSubject")
