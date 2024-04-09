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


#BUILD THE URL
def get_url(city):
    #api key
    api_key = get_api_key()

    #url encoded city name
    city_name = parse.quote_plus(city)

    #the url 
    url = (f"{base_url}?q={city_name}&appid={api_key}")
    return url

#GET DATA FROM THE URL
def get_data(url):
    #create a request object and add a user-agent
    req = request.Request(url, headers={'User-Agent':'Mozilla/5.0'})

    #initialting the http request from the request object
    try:
        response = request.urlopen(req)
    except error.HTTPError as http_error:
        #401 Unauthorized
        if http_error.code == 401:
            sys.exit("Access Denied, Check your API key.")
         #401 Not-Found
        elif http_error.code == 404:
            sys.exit("Can't find the data for the mentioned city.")
        else: 
            sys.exit(f"Something went wrong... ({http_error.code})")
    
    #reading data from the response
    data = response.read()

    #return deserialized json
    try:
        return json.loads(data)
        
    #unless.. there is an error 
    except:
         sys.exit("Couldn't read the server response")

    

    
    

