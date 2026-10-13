
# ---------------------------------------------------------
# 1. IMPORT LIBRARIES
# ---------------------------------------------------------

# Requests allows us to communicate with an API
import requests

# Datetime allows us to work with dates
from datetime import datetime


# ---------------------------------------------------------
# 2. USER SETTINGS
# ---------------------------------------------------------

# Our Pixela account information
USERNAME = 'mynameisdiogo'
TOKEN = 'hhasdalkkadsda'
GRAPH = "graph1"

# Main URL for the Pixela API
pixela_endpoint = 'https://pixe.la/v1/users'


# ---------------------------------------------------------
# 3. CREATE A USER
# ---------------------------------------------------------

# Information needed to create a new Pixela account
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# POST sends information to the API to create a new user
# Commented out because we only need to create the user once

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# ---------------------------------------------------------
# 4. CREATE A GRAPH
# ---------------------------------------------------------

# URL for creating graphs under our username
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Settings for our graph
graph_config = {
    "id": GRAPH,
    "name": "Coding Graph",
    "unit": "H",
    "type": "float",
    "color": "sora"
}

# Headers contain our token to identify our account
headers = {
    "X-USER-TOKEN": TOKEN
}

# POST creates a new graph
# Commented out because the graph already exists

# response = requests.post(
#     url=graph_endpoint,
#     json=graph_config,
#     headers=headers
# )
# print(response.text)


# ---------------------------------------------------------
# 5. ADD A PIXEL TO THE GRAPH
# ---------------------------------------------------------

# URL used to add a pixel to our graph
graph_pixel_id = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

# Select the date we want to record
today = datetime(year=2026, month=10, day=11)

# Information for the new pixel
graph_pixel = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15"
}

# strftime converts our date into the format YYYYMMDD
# Example: 11 October 2026 becomes 20261011

# POST creates a new pixel for the selected date
# Commented out so it does not run automatically

# response = requests.post(
#     url=graph_pixel_id,
#     json=graph_pixel,
#     headers=headers
# )
# print(response.text)


# ---------------------------------------------------------
# 6. UPDATE AN EXISTING PIXEL
# ---------------------------------------------------------

# Choose the date of the pixel we want to update
date_to_update = datetime(year=2026, month=10, day=11)

# URL pointing to that specific pixel
graph_pixel_id = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{date_to_update.strftime('%Y%m%d')}"

# New quantity for the selected date
update_graph_pixel = {
    "quantity": "10"
}

# PUT changes the value of an existing pixel
# Commented out so it does not run automatically

# response = requests.put(
#     url=graph_pixel_id,
#     json=update_graph_pixel,
#     headers=headers
# )
# print(response.text)


# ---------------------------------------------------------
# 7. DELETE AN EXISTING PIXEL
# ---------------------------------------------------------

# Choose the date of the pixel we want to delete
delete_pixel = datetime(year=2026, month=10, day=11)

# URL pointing to the pixel we want to remove
delete_graph_pixel_id = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{delete_pixel.strftime('%Y%m%d')}"

# DELETE removes the pixel from our graph
# This is the active request in our script

response = requests.delete(
    url=delete_graph_pixel_id,
    headers=headers
)

# Print the response to check whether it worked
print(response.text)
