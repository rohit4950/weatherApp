import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()
api_key = os.getenv('API_KEY')

@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: float

def getlanlon(city_name, API_key):
    res = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={API_key}').json()
    data = res[0]
    lat, lon = data.get('lat'), data.get('lon')
    return lat, lon

def get_currentweather(lat, lon, API_key):
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()
    data = WeatherData(
        main=res.get('weather')[0].get('main'),
        description=res.get('weather')[0].get('description'),
        icon=res.get('weather')[0].get('icon'),
        temperature=res.get('main').get('temp')
    )
    return data

def main(city_name):
    lat, lon = getlanlon(city_name, api_key) 
    weather_data = get_currentweather(lat, lon, api_key)
    return weather_data

if __name__ == "__main__":
    city_name = input("Enter city name: ")  
    print(main(city_name))  