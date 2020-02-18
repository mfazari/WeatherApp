import urllib
from flask import Flask, jsonify
import os
import json
import urllib.request
import urllib.error

# global variables
status = "undefined"
api_key = os.environ['api_key']


# Routes
def configure_routes(app):
    @app.route('/forecast/<city>', methods=['GET'])
    def weather(city):
        link = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key
        try:
            response = urllib.request.urlopen(link)
            set_status("ok")
            dictionary = json.load(response)
            return jsonify(
                clouds=cloud_status(dictionary),
                humidity=humidity_status(dictionary),
                pressure=pressure_status(dictionary),
                temperature=temperature_status(dictionary)
            )
        except urllib.error.HTTPError as e:
            if e.code == 401:
                set_status("401 error")
                return jsonify(
                    error="unauthorized",
                    error_code="unauthorized request"
                )
            elif e.code == 404:
                set_status("404 error")
                return jsonify(
                    error="Cannot find city " + city,
                    error_code="city not found"
                )
            elif e.code == 500:
                set_status("500 error")
                return jsonify(
                    error="Something went wrong",
                    error_code="internal server error"
                )
            elif e.code == 429:
                set_status("429 error")
                return jsonify(
                    error="Too many API calls",
                    error_code="API calls overload"
                )

    # Error route in case no city is provided throws 400
    @app.route('/forecast/')
    def no_input():
        return jsonify(
            error="no city provided",
            error_code="invalid request",
        ), 400

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
    temperature_kelvin = data.get('main', {}).get('temp')
    temperature_celsius = str(round(temperature_kelvin - 273.15, 1)) + "C"
    return temperature_celsius


# Returns Version Number from Version file
def get_version():
    k = open('VERSION')
    version_number = k.readline()
    k.close()
    return version_number


# Sets Status
def set_status(status_code):
    global status
    status = status_code
