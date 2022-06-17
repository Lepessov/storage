import requests
from bs4 import BeautifulSoup

key = 'f584e8a357643519edeee4e652b3e1c0'

weather_params = {
        'lat': 43.222015,
        'lon': 76.851250,
        'appid': key,
        'exlcude': 'current,minutely,daily'
        }
x = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=weather_params)

print(x.content())

