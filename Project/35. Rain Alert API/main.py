import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "a94fcccf9438b12e06604d4e10585d71"

weather_params = {
    "lat": 22.393420,
    "lon": 91.821540,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
# print(response.status_code)
# print(response.json())
weather_data = response.json()
# print(weather_data)
# print(weather_data["hourly"][0]["weather"][0]["id"])
weather_slice = weather_data["hourly"][:12]
# print(weather_slice)

will_rain = False
for hour_data in weather_slice:
    # print(hour_data["weather"][0]["id"])
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        # print("Bring an Umbrella.")
        will_rain = True

if will_rain:
    print("Bring an Umbrella.")
