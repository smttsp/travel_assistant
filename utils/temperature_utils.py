"""https://openweathermap.org/api/one-call-3
This looks nice
"""

import requests, json


def get_temperature_for_location():
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = "Hyderabad"
    API_KEY = "Your API Key"
    # updating the URL
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    # HTTP request
    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200:
       data = response.json()
       main = data['main']
       temperature = main['temp']
       humidity = main['humidity']
       pressure = main['pressure']
       report = data['weather']
       print(f"{CITY:-^30}")
       print(f"Temperature: {temperature}")
       print(f"Humidity: {humidity}")
       print(f"Pressure: {pressure}")
       print(f"Weather Report: {report[0]['description']}")
    else:
       print("Error in the HTTP request")


from math import radians, sin, cos, sqrt, atan2

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in kilometers

    # Convert latitude and longitude to radians
    lat1_rad, lon1_rad = radians(lat1), radians(lon1)
    lat2_rad, lon2_rad = radians(lat2), radians(lon2)

    # Calculate the differences between the latitudes and longitudes
    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    # Apply the Haversine formula to calculate the distance
    a = sin(delta_lat/2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(delta_lon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c

    return distance


def search_nearby_locations(target_lat, target_lon, cache):
    nearby_locations = []

    for location in cache:
        lat, lon = location["latitude"], location["longitude"]
        distance = calculate_distance(target_lat, target_lon, lat, lon)

        if distance <= 10:
            nearby_locations.append(location)

    return nearby_locations
