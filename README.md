Weather service
===============


Introduction
------------

This is an HTTP service which provides an API to get a weather
forecast for a given city.

The [openweathermap](https://www.openweathermap.org) is being used as API. The API requires an API key that can be obtained for free
after [signing up](https://home.openweathermap.org/users/sign_up)

Getting it running
------------------

1. Open Terminal
2. Go to the project directory via cd
3. This app uses flask for routing. There are other choices like Django, but we want to keep it simple. We need to install it:

    ```
    pip install flask
    ``` 

4. If you're not familiar with enviromental variables, read [this](https://towardsdatascience.com/how-to-hide-your-api-keys-in-python-fb2e1a61b0a0).
5. Take your API Key (from openweathermap) and set it as 'api_key'.
6. Run script with

    ```
    python app.py
    ```

How to run tests:
1. Install pytest
    ```
    pip install -U pytest
    ```
2. Run with
    ```
    pytest
    ```

Calls
-----------

You can use [curl](https://curl.haxx.se/) to test the following calls:

### `/ping`

This is a simple health check that we can use to determine that the service is
running, and provides information about the application.

```bash
$ curl -si http://localhost:8080/ping

HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
{
  "name": "weatherservice",
  "status": "ok",
  "version": "1.0.0"
}
```

### `/forecast/<city>`


Fetching the weather data for Manchester:

```bash
$ curl -si http://localhost:8080/forecast/Manchester/

HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
{
    "clouds": "broken clouds",
    "humidity": "66.6%",
    "pressure": "1027.51 hPa",
    "temperature": "14.4C"
}
```

### Errors

Error messages will look like this:

```bash
$ curl -si http://localhost:8080/forecast/ldakfjdöfa

HTTP/1.1 404 Not Found
Content-Type: application/json; charset=utf-8
{
    "error": "Cannot find country 'ldakfjdöfa'",
    "error_code": "country not found"
}
```

