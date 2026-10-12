import requests
from datetime import datetime

USERNAME = 'mynameisdiogo'
TOKEN = 'hhasdalkkadsda'
GRAPH = "graph1"

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    "token": "USERNAME",
    "username": "TOKEN",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "GRAPH",
    "name": "Coding Graph",
    "unit": "H",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

graph_pixel_id = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

today = datetime(year=2026, month=10, day=11)

graph_pixel = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15"

}

# response = requests.post(url=graph_pixel_id, json=graph_pixel,  headers=headers)
# print(response.text)



date_to_update = datetime(year=2026, month=10, day=11)


graph_pixel_id = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{date_to_update.strftime('%Y%m%d')}"

update_graph_pixel = {
    "quantity": "10"
}

# response = requests.put(url=graph_pixel_id, json=update_graph_pixel,  headers=headers)
# print(response.text)

delete_pixel = datetime(year=2026, month=10, day=11)

delete_graph_pixel_id = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{delete_pixel.strftime('%Y%m%d')}"

response = requests.delete(url=graph_pixel_id, json=delete_graph_pixel_id,  headers=headers)
print(response.text)