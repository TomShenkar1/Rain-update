import requests
from twilio.rest import Client

MYLAT = YOUR LATITUDE
MYLONG = YOUR LONGITUDE
api_key = "b2e75fb06a6ab5809cf6a28abc56c7e7"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "AC7612272defdc4b3a2619fe0944504935"
auth_token = "YOUR AUTH TOKEN"
parameters = {
    "lat": MYLAT,
    "lon": MYLONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

hours_list = weather_data["hourly"][:12]

for hour in hours_list:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
    else:
        will_rain = False

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Hey Tom! it is going to rain today, remember to take an ☂️",
        from_= "TWILIO NUMBER",
        to="YOUR PHONE NUMBER"
    )



