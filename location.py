import os
import urllib
import json


def location_route():
    link = "http://api.ipstack.com/80.254.78.161?access_key=" + os.environ['ACCESS_KEY']
    response = urllib.request.urlopen(link)
    data = json.load(response)
    city = data.get('city')
    return city
