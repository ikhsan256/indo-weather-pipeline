import requests
import json
from datetime import datetime

def fetch_weather(api_url, api_key):
    response = requests.get(f"{api_url}?apikey={api_key}")
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        return None

def save_weather_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

if __name__ == "__main__":
    API_URL = "http://mockweatherapi.com/weather"
    API_KEY = "your_api_key_here"
    weather_data = fetch_weather(API_URL, API_KEY)
    if weather_data:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"weather_data_{timestamp}.json"
        save_weather_data(weather_data, filename)
        print(f"Weather data saved to {filename}")
    else:
        print("Failed to fetch weather data")
