import os
import requests
from geopy.geocoders import Nominatim

def getLocation(city, state, country):
    geoloactor = Nominatim(user_agent="Weather App")
    locationString = '{} {} {}'.format(city, state, country)
    location = geoloactor.geocode(locationString)
    return location

def getCurrentWeather(lat, long):
    reqUrl = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=imperial'.format(lat, long, os.environ.get('OPENWEATHER_API_KEY'))
    weather = requests.get(reqUrl).json()
    return weather