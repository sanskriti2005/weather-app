import click
import os
from urllib import parse, request, error
import json
import sys

#API KEY ENVIRONEMENT VARIABLE
def get_api_key():
    return os.getenv("OpenWeatherAPI")

#ARGUMENTS
@click.command()
@click.argument('city')
@click.option('-p','--pressure', help='gets the pressure data for the entered city.')
@click.option('-h', '--humidity', help='gets the humidity data for the entered city.')


