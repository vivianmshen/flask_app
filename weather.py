import forecastio
from geopy.geocoders import Nominatim
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

#lat = 37.77
#lng = -122.43

#forecast = forecastio.load_forecast(api_key, lat, lng).currently()


#for forecasts in forecast.daily().data:
#	print(forecasts.precipProbability)

def get_latitude(address):
	geolocator = Nominatim()
	return geolocator.geocode(address).latitude

def get_longitude(address):
	geolocator = Nominatim()
	return geolocator.geocode(address).longitude

def get_weather(address):
	api_key = os.environ['FORECASTIO_API_KEY']
	lat = get_latitude(address)
	lng = get_longitude(address)
	forecast = forecastio.load_forecast(api_key, lat, lng).currently()
	return "The weather is {} and {} degrees".format(forecast.summary, forecast.temperature)

#address = input("What is the address you would like the weather for? ")
#print(get_weather(address, "key"))