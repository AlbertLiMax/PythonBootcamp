import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# Raise exception if there are error status codes
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)