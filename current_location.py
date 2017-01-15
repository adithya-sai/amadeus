import urllib2

import json

# Automatically geolocate the connecting IP
def get_location():

    f = urllib2.urlopen('http://freegeoip.net/json/')
    json_string = f.read()
    f.close()
    location = json.loads(json_string)
    location_city = location['city']
    # location_state = location['region_name']
    #
    # location_country = location['country_name']
    #
    # location_zip = location['zip_code']
    return location_city