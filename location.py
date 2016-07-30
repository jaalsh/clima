import weatherparser, weathermath

class Location:

        def __init__(self, name, lat, lng, altitude, weather, forecast):
            self.name = name
            self.lat = lat
            self.lng = lng
            self.altitude = altitude
            self.weather = weather
            self.forecast = forecast

        def display(self):
            station_location = weatherparser.WeatherParser(self.weather).parse_location()
            distance = weathermath.haversine(self.lng, self.lat, station_location['lon'], station_location['lat'])
            print("Name: %s\tLat: %.3f\tLng: %.3f\tAlt: %.3fm\tStation Distance: %.3fkm" %(self.name, self.lat, self.lng, self.altitude, distance))
