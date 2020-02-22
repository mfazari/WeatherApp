# Execute file with pytest
from flask import Flask
from routes import configure_routes


# Test existing city
def test_weather_1():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/forecast/London'

    response = client.get(url)
    assert response.status_code == 200


# Test no city provided
def test_weather_2():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/forecast/'

    response = client.get(url)
    assert response.status_code == 400
