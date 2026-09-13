import datetime as dt
import csv
from pathlib import Path
import random
import smtplib


# Get today's date
now = dt.datetime.now()


# Load all letter templates into a list
letters = []

folder = Path("letter_templates")

for file in folder.iterdir():
    letters.append(file)


# Email account details
my_email = "YOUR_EMAIL"
password = "YOUR_PASSWORD"


# Open the birthday CSV file
with open("birthdays.csv") as file:
    data = csv.DictReader(file)

    # Check each person in the CSV
    for row in data:

        # Check if today matches their birthday
        if now.day == int(row["day"]) and now.month == int(row["month"]):

            # Pick a random birthday letter
            with open(random.choice(letters)) as letter_file:
                email = letter_file.read()

            # Replace [NAME] with the person's name
            email_replace = email.replace("[NAME]", row["name"])

            # Send the birthday email
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)

                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=row["email"],
                    msg=f"Subject:Happy Birthday\n\n{email_replace}"
                )

            print(email_replace)