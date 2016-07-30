from math import radians, sin, cos, asin, sqrt

def kelvin_to_celcius(k):
    return k - 273.15

def ms_to_mph(ms):
    return ms * 2.23694

def deg_to_cardinal(deg):
    cardinals = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                 "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW", "N"]
    return cardinals[int(round((deg*10) % 3600 / 225))]

def haversine(lat1, lng1, lat2, lng2):
    # covert from decimal degrees to radians
    lat1, lng1, lat2, lng2 = map(radians, (lat1, lng1, lat2, lng2))
    # haversine formula
    lat = lat2 - lat1
    lng = lng2 - lng1
    d = 2 * asin(sqrt(sin(lat * 0.5) ** 2 + cos(lat1) * cos(lat2) * sin(lng * 0.5) ** 2))
    # * by 6371 (earth radius in km) to get km
    return 6371 * d
