import os, json, location, webreader, datetime, weathermath

def save_file(loc):
    d = {'name':loc.name, 'lat':loc.lat, 'lng':loc.lng, 'altitude':loc.altitude}
    json.dump(d, open(loc.name  + '.txt', 'x'))
    print("Creating file...")

def read_file(location_name):
    print("Reading file...")
    d = json.load(open(location_name + ".txt"))
    lat = d['lat']
    lng = d['lng']
    weather = webreader.read_weather_from_latlng(lat, lng)
    forecast = webreader.read_forecast_from_latlng(lat, lng)
    stations = webreader.read_stations_from_latlng(lat, lng)
    return location.Location(d['name'], lat, lng, d['altitude'], weather, forecast, stations)

def file_exists(location_name):
    file_path = os.path.dirname(os.path.realpath(__file__))
    if os.path.isfile(location_name + '.txt'):
        return True
    return False

def write_forecast_to_file(loc, count):
    for i, e in enumerate(loc.forecast['list']):
        if i >= loc.forecast['cnt'] or i >= count:
            break
        with open(loc.name + '_forecast_' + datetime.datetime.now().strftime('%d%m%Y%H%M%S') + '.txt', 'a') as forecast_file:
            timestamp = datetime.datetime.utcfromtimestamp(e['dt']).strftime('%d-%m-%Y %H:%M:%S')
            temp = weathermath.kelvin_to_celcius(e['main']['temp'])
            temp_min = weathermath.kelvin_to_celcius(e['main']['temp_min'])
            temp_max = weathermath.kelvin_to_celcius(e['main']['temp_max'])
            pressure = e['main']['pressure']
            humidity = e['main']['humidity']
            desc = e['weather'][0]['description']
            clouds = e['clouds']['all']
            wind_speed = weathermath.ms_to_mph(e['wind']['speed'])
            wind_deg = weathermath.deg_to_cardinal(e['wind']['deg'])
            forecast_file.write("\n%s\nDescription: %s\nTemp: %.2fc\nMin Temp: %.2fc\nMax Temp: %.2fc\nPressure: %.2fhPa\nHumidity: %.2f%%\nClouds: %.2f%%\nWind Speed: %.2fmph\nWind Deg: %s\n"
                    % (timestamp, desc, temp, temp_min, temp_max, pressure, humidity, clouds, wind_speed, wind_deg))
