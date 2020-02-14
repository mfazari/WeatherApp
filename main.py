from flask import Flask, jsonify, redirect, url_for, request
import os
app = Flask(__name__)


# global variables
status = "undefined"


# Routes
@app.route('/forecast/<city>', methods=['GET'])
def weather(city):
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


# Returns Status Number from Version file
def set_status(argument):
    status = argument


# Running our little server
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
