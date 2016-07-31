import requests, json

owm_api_key = 'YOUR_KEY' #TODO: enter your key here
STATION_COUNT = 5

class WebReader:

    def __init__(self, location_name):
            self.lat_lng = self.read_lat_lng(location_name)
            self.lat = self.lat_lng['lat']
            self.lng = self.lat_lng['lng']
            self.altitude = self.read_altitude()
            self.weather = self.read_weather()
            self.forecast = self.read_forecast()
            self.stations = self.read_stations()

    def read_lat_lng(self, location_name):
        response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=%s' % location_name)
        return response.json()['results'][0]['geometry']['location']

    def read_altitude(self):
        response = requests.get('https://maps.googleapis.com/maps/api/elevation/json?locations=%f,%f' %(self.lat, self.lng))
        return response.json()['results'][0]['elevation']

    def read_weather(self):
        response = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=%f&lon=%f&appid=%s' %(self.lat, self.lng, owm_api_key))
        return response.json()

    def read_forecast(self):
        response = requests.get('http://api.openweathermap.org/data/2.5/forecast?lat=%f&lon=%f&appid=%s' %(self.lat, self.lng, owm_api_key))
        return response.json()

    def read_stations(self):
        response = requests.get('http://api.openweathermap.org/data/2.5/station/find?lat=%f&lon=%f&cnt=%d&appid=%s' %(self.lat, self.lng, STATION_COUNT, owm_api_key))
        return response.json()

def read_weather_from_latlng(lat, lng):
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=%f&lon=%f&appid=%s' %(lat, lng, owm_api_key))
    return response.json()

def read_forecast_from_latlng(lat, lng):
    response = requests.get('http://api.openweathermap.org/data/2.5/forecast?lat=%f&lon=%f&appid=%s' %(lat, lng, owm_api_key))
    return response.json()

def read_stations_from_latlng(lat, lng):
    response = requests.get('http://api.openweathermap.org/data/2.5/station/find?lat=%f&lon=%f&cnt=%d&appid=%s' %(lat, lng, STATION_COUNT, owm_api_key))
    return response.json()
