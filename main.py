import urllib
from collections import namedtuple

from flask import Flask, jsonify, redirect, url_for, request
import os
import json
import urllib.request as request

app = Flask(__name__)

# global variables
status = "undefined"
api_key = os.environ['api_key']


# Routes
@app.route('/forecast/<city>', methods=['GET'])
def weather(city):
    link = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key
    with request.urlopen(link) as response:
        if response.getcode() == 200:
            set_status("ok")
            dictionary = json.load(response)
            # temporary_data = json.dumps(dictionary)
            # data = jsonify(temporary_data)
            return jsonify(
                clouds=cloud_status(dictionary),
                humidity=humidity_status(dictionary),
                pressure=pressure_status(dictionary),
                temperature=temperature_status(dictionary)
            )
        elif response.getcode() == 400:
            set_status("error")
            return jsonify(
                error="no city provided",
                error_code="invalid request"
            )
        elif response.getcode() == 401:
            set_status("error")
            return jsonify(
                error="unauthorized",
                error_code="unauthorized request"
            )
        elif response.getcode() == 404:
            set_status("error")
            return jsonify(
                error="Cannot find city" + city,
                error_code="city not found"
            )
        elif response.getcode() == 500:
            set_status("error")
            return jsonify(
                error="Something went wrong",
                error_code="internal server error"
            )
        elif response.getcode() == 429:
            set_status("error")
            return jsonify(
                error="Too many API calls",
                error_code="API calls overload"
            )


@app.route('/ping')
def ping():
    return jsonify(
        name="weatherservice",
        status=status,
        version=get_version()
    )


# Weather functions
def cloud_status(data):
    temp = data.get('clouds', {}).get('all')
    print(temp)
    if 10 >= temp >= 0:
        return "clear sky"
    elif 36 >= temp > 10:
        return "few clouds"
    elif 60 >= temp > 37:
        return "scattered clouds"
    elif 84 >= temp > 61:
        return "broken clouds"
    elif 100 >= temp > 85:
        return "overcast"
    else:
        return "invalid data"


def humidity_status(data):
    value = data.get('main', {}).get('humidity')
    humidity = str(value) + "%"
    return humidity


def pressure_status(data):
    value = data.get('main', {}).get('pressure')
    pressure = str(value) + " hPa"
    return pressure


def temperature_status(data):
    value = data.get('main', {}).get('temp')
    temperature_celsius = value - 273.15
    return temperature_celsius


# Returns Version Number from Version file
def get_version():
    k = open('VERSION')
    version_number = k.readline()
    k.close()
    return version_number


# Sets Status
def set_status(status_code):
    status = status_code


# Running our little program
if __name__ == '__main__':
    app.run(debug=True, port=8080)
