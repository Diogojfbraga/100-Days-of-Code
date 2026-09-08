import datetime as dt
import random
import smtplib

now = dt.datetime.now()

quotes = []


my_email = "d######t@gmail.com"
## Generate the app password in google > security
passoword = "### # ## # # #"


with open("quotes.txt") as file:

    for quote in file:
        quotes.append(quote)

quote_of_the_day = random.choice(quotes)

if now.weekday() == 1:
    print(random.choice(quotes))
    with smtplib.SMTP("smtp.gmail.com") as connection:

        connection.starttls()
        connection.login(user=my_email, password=passoword)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="####@gmail.com", 
            msg=f"Subject:Hello\n\n{quote_of_the_day}")

        connection.close()
    
    