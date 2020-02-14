from flask import Flask, jsonify, redirect, url_for, request
import os
import json
import urllib.request as request
app = Flask(__name__)


# global variables
status = "undefined"
api_key = os.environ['api_key'];


# Routes
# TODO add routes for error
@app.route('/forecast/<city>', methods=['GET'])
def weather(city):
    link = "api.openweathermap.org/data/2.5/weather?q={" + city + "}&appid={" + api_key + "}"
    with request.urlopen(link) as response:
        if response.getcode() == 200:
            source = response.read()
            data = json.loads(source)
        else:
            print('An error occurred while attempting to retrieve data from the API.')
    return jsonify(
        clouds="",
        humidity="",
        pressure="",
        temperature=""
    )


@app.route('/ping', method=['GET'])
def ping():
    return jsonify(
        name="weatherservice",
        status=status,
        version=get_version()
    )


# Returns Version Number from Version file
def get_version():
    k = open('VERSION')
    version_number = k.readline()
    k.close()
    return version_number


# Sets Status
def set_status(argument):
    status = argument

#

# Running our little program
if __name__ == '__main__':
    print(os.environ['public_key'])
    app.run(debug=True, port=8080)

'''
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

'''
