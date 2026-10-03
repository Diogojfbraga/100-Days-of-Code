import requests

USERNAME = 'mynameisdiogo'
TOKEN = 'hhasdalkkadsda'

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
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "H",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

print(response.text)
