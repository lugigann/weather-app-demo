# import json
#
# from flask import Flask
#
# import weather
#
#
# app = Flask(__name__)
#
# @app.route("/")
# def hello():
#     return "Hello, World!"
#
# @app.route("/weather/")
# def weather_rout():
#     temp = weather.weather()
#     temp = json.dumps(weather.weather())
#     return temp
#
# @app.route("/weather/my-cities/")
# def weather_multiple_cities():
#     return "Cluj: 15, New York: 10"
# # We use python module requests to communicate and get data from websites
# import requests
#
# # Gets the current location's city name by IP adress
# ipAddress = requests.get('https://api.ipify.org').text
#
# # Creates a dictionary from which we extract the name of city we're in based on our location's IP.
# # To see how this dictionary looks, copy the following link and paste it in your web browser. (try a JSON addon readability)
# # Don't fortget to substitute '{ipAdress}' with the name of a city e.g. Bucharest, Cluj-Napoca
# res = requests.get(f'http://api.ipstack.com/{ipAddress}?access_key=af0d2f12457ae7f68e463692487a987f').json()
#
# place = res['city']
#
# # Gets weather data on the current location by city name
# # If you want to see the temperature in Fahrenheit, replace 'metric' with 'imperial'
# # Copy the following link in your browser to see how its dictionary looks. (try a JSON addon readability)
# data = requests.get('http://api.openweathermap.org/data/2.5/'
#                     'weather?q={}&appid=271d1234d3f497eed5b1d80a07b3fcd1&units=metric'.format(place)).json()
#
# # Few details about the weather
# temp = data['main']['temp']
# description = data['weather'][0]['description']
#
# # Weather display
# w_details = (f'Temperature: {str(temp)} degrees \nStatus: {description}')

import json
from flask import  Flask #importa obiectul Flask din modulul flask
import weather
# import sys
# print(">>", sys.path()) #nu este corect definit
app = Flask(__name__)
@app.route("/") # / inseamna ca ruleaza din root
def hello():
   return "Hello,World!"
@app.route("/weather/") # atentie la /weather/ sa fie intre back slah sau calea buna
def weather_route(): #numele la aceasta functie trebuie sa fie diferit de numele la functia importata
   temp = json.dumps(weather.weather())
   return temp
@app.route("/weather/my-cities/") #route defineste ruta
def weather_multiplecities():
   return "Cluj: 15, New Yourk: 10"