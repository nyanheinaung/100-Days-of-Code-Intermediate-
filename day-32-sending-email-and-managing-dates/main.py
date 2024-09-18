import smtplib

my_email = "testforlearning12@gmail.com"
password = "hdix ewbu conu dizo "
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="testforlearning12@yahoo.com", msg="Hello")
connection.close()
