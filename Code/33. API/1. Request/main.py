import requests

response = requests.get(url="http://api.open-notify.org/iss-now/json")
print(response)
print(response.status_code)

# TODO: Error
response.raise_for_status()

# TODO: json
data = response.json()
# print(data)
# data = response.json()["iss_position"]["longitude"]
# print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)
