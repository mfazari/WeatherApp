from flask import Flask, redirect, url_for, request

app = Flask(__name__)
import os


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


# Routes
@app.route('/login', methods=['GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


# Running our little server
if __name__ == '__main__':
    print(os.environ['public_key'])
    app.run(debug=True, port=8080)

