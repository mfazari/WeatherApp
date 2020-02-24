from flask import Flask
from routes import configure_routes

app = Flask(__name__)

configure_routes(app)


# Running on port 8080
if __name__ == '__main__':
    app.run(port=8080)
