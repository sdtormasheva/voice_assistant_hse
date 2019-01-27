import requests
import json
from urllib.parse import urlencode
from modules import auth_keys


def get_current_geo():
    url = "https://www.googleapis.com/geolocation/v1/geolocate?key=" + auth_keys.key
    payload = {
        "considerIp": "true",
        "wifiAccessPoints": []
    }
    r = requests.post(url, json=payload)
    resp = json.loads(r.text)
    if 'location' in resp:
        return resp['location']
    else:
        return None


def get_geo(address):
    params = {'address': address, 'language': 'ru', 'key': auth_keys.key}
    link = 'https://maps.googleapis.com/maps/api/geocode/json?'
    url = link + urlencode(params)
    r = requests.get(url)
    result = json.loads(r.text)
    if result['status'] == "OK":
        location_geo = result['results'][0]['geometry']['location']
        location_name = result['results'][0]['formatted_address']
        # location_name_components = result['results'][0]['address_components']
        # for comp in location_name_components:
        #     if "political" not in comp['types']:
        #         location_name.append(comp['long_name'])
        #     else:
        #         break
        # location_name = ' '.join(location_name[::-1])
        return location_geo, location_name
    else:
        return None


def get_address(latlng):
    point = str(latlng['lat']) + ',' + str(latlng['lng'])
    params = {'address': point, 'language': 'ru', 'result_type': 'street_address', 'key': auth_keys.key}
    link = 'https://maps.googleapis.com/maps/api/geocode/json?'
    url = link + urlencode(params)
    r = requests.get(url)
    result = json.loads(r.text)
    if result['status'] == "OK":
        location_name = result['results'][0]['formatted_address']
        return location_name
    else:
        return None
