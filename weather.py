import click
import os
from urllib import parse, request, error
import json
import sys

#API KEY ENVIRONEMENT VARIABLE
def get_api_key():
    return os.getenv("OpenWeatherMapAPI")

#BASE URL TO CREATE THE URL
base_url = "https://api.openweathermap.org/data/2.5/weather"

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


#ARGUMENTS
@click.command()
#takes argument for the city
@click.argument('city')

#takes an optional argument to give pressure data
@click.option('-p','--pressure', default=None,is_flag=True, help='gets the pressure data for the entered city.')

#takes an optional argument to give humidity data
@click.option('-h', '--humidity', default=None,is_flag=True, help='gets the humidity data for the entered city.')

def main(city, pressure=False, humidity=False):
    #GET THE URL
    query_url = get_url(city)

    #GET THE DATA FROM THE URL
    data = get_data(query_url)

    # Extract the required information from the data
    city_name = data.get('name')
    country_name = data.get('sys', {}).get('country')
    temperature = data.get('main', {}).get('temp')
    description = data.get('weather', [{}])[0].get('description')

    # Print the required information
    print(f"City: {city_name}")
    print(f"Country: {country_name}")
    print(f"Temperature: {temperature}")
    print(f"Weather Description: {description}")

    # If pressure option is set, print the pressure
    if pressure:
        pressure_value = data.get('main', {}).get('pressure')
        print(f"Pressure: {pressure_value}")

    # If humidity option is set, print the humidity
    if humidity:
        humidity_value = data.get('main', {}).get('humidity')
        print(f"Humidity: {humidity_value}")
   
if __name__ == "__main__":
    main()
    






