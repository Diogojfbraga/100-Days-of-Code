
import os
import smtplib
import requests

from bs4 import BeautifulSoup
from dotenv import load_dotenv
from pathlib import Path


# ---------------------------------------------------------
# 1. CONFIGURATION
# ---------------------------------------------------------

AMAZON_URL = "https://appbrewery.github.io/instant_pot/"
BUY_PRICE = 100.00

# Load environment variables from the project's .env file
load_dotenv(Path(__file__).resolve().parent / ".env")

SMTP_ADDRESS = os.environ["SMTP_ADDRESS"]
EMAIL_ADDRESS = os.environ["EMAIL_ADDRESS"]
EMAIL_PASSWORD = os.environ["EMAIL_PASSWORD"]


# ---------------------------------------------------------
# 2. FETCH AMAZON PRODUCT PAGE
# ---------------------------------------------------------

response = requests.get(AMAZON_URL, timeout=15)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")


# ---------------------------------------------------------
# 3. EXTRACT PRODUCT INFORMATION
# ---------------------------------------------------------

# Extract product title
title = soup.find(id="productTitle").get_text(strip=True)

# Extract whole and decimal portions of the price
whole_price = soup.find(class_="a-price-whole").get_text().strip(".")
fraction_price = soup.find(class_="a-price-fraction").get_text(strip=True)

# Convert price to a float
price = float(f"{whole_price}.{fraction_price}")

print(f"Product: {title}")
print(f"Current Price: £{price:.2f}")
print(f"Target Price: £{BUY_PRICE:.2f}")


# ---------------------------------------------------------
# 4. CHECK PRICE AGAINST TARGET
# ---------------------------------------------------------

if price <= BUY_PRICE:

    message = (
        f"{title} is on sale!\n\n"
        f"Current price: {price:.2f}\n"
        f"Target price: {BUY_PRICE:.2f}\n\n"
        f"Buy here: {AMAZON_URL}"
    )

    # -----------------------------------------------------
    # 5. SEND EMAIL NOTIFICATION
    # -----------------------------------------------------

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:

        # Secure the connection
        connection.starttls()

        # Log in to email account
        connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        # Send price alert email
        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs=EMAIL_ADDRESS,
            msg=(
                f"Subject: Amazon Price Alert!\n"
                f"Content-Type: text/plain; charset=utf-8\n\n"
                f"{message}"
            ).encode("utf-8")
        )

    print("Price alert email sent successfully!")

else:
    print("Price is still above target. No email sent.")
