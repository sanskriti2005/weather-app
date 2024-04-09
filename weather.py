import click
import os
from urllib import parse, request, error
import json
import sys

#API KEY ENVIRONEMENT VARIABLE
def get_api_key():
    return os.getenv("OpenWeatherAPI")


#BASE URL TO CREATE THE URL
base_url = "https://api.openweathermap.org/data/2.5/weather"


#ARGUMENTS
@click.command()
@click.argument('city')
@click.option('-p','--pressure', help='gets the pressure data for the entered city.')
@click.option('-h', '--humidity', help='gets the humidity data for the entered city.')

def get_url(city):
    #api key
    api_key = get_api_key()

    #url encoded city name
    city_name = parse.quote_plus(city)

    #the url 
    url = (f"{base_url}?q={city_name}&appid={api_key}")
    return url

