import json

from flask import Flask

import weather

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/weather/")
def weather_rout():
    temp = weather.weather()
    temp = json.dumps(weather.weather())
    return temp

@app.route("/weather/my-cities/")
def weather_multiple_cities():
    return "Cluj: 15, New York: 10"