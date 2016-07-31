import os, json, location, webreader

#TODO: ADD ABILITY TO PRINT TO TEXT FILE SO YOU CAN HAVE LOCAL COPY TO PRINT ON PAPER ETC.

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
