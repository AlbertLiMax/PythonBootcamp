import requests
from datetime import datetime

TOKEN = "pythonbootcamptest"
USERNAME = "albertlimax"
GRAPH = "readinggraph1"
pixela_endpoint = "https://pixe.la/v1/users/"

# # Create an pixela account
# user_params = {
#     "token": TOKEN,
#     "username" : USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
#
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
#
# # Create an pixela graph
# pixela_graph_endpoint = pixela_endpoint + USERNAME + "/graphs"
#
# graph_config = {
#     "id": GRAPH,
#     "name": "Reading Graph",
#     "unit": "Page",
#     "type": "int",
#     "color": "sora"
# }
#
headers = {
    "X-USER-TOKEN": TOKEN
}
#
# response = requests.post(url=pixela_graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
#
# Add a pixel
pixela_pixel_endpoint = pixela_endpoint + USERNAME + "/graphs/" + GRAPH

today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many pages of book have you read today? "),
}

response = requests.post(url=pixela_pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)
#
# # Update a pixel
# date = datetime.now().strftime("%Y%m%d")
#
# pixela_pixel_update_endpoint = pixela_endpoint + USERNAME + "/graphs/" + GRAPH + "/" + date
#
# pixel_update_config = {
#     "quantity": "36",
# }
#
# response = requests.put(url=pixela_pixel_update_endpoint, json=pixel_update_config, headers=headers)
# print(response.text)
#
# Delete a pixel
# date = datetime.now().strftime("%Y%m%d")
#
# pixela_pixel_update_endpoint = pixela_endpoint + USERNAME + "/graphs/" + GRAPH + "/" + date
#
# response = requests.delete(url=pixela_pixel_update_endpoint, headers=headers)
# print(response.text)
