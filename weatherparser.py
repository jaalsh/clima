import webreader, datetime, weathermath

class WeatherParser:

    def __init__(self, weather):
        self.weather = weather

    def parse_location(self):
        return self.weather['coord']

    def display(self):
            timestamp = datetime.datetime.utcfromtimestamp(self.weather['dt']).strftime('%d-%m-%Y %H:%M:%S')
            temp = weathermath.kelvin_to_celcius(self.weather['main']['temp'])
            temp_min = weathermath.kelvin_to_celcius(self.weather['main']['temp_min'])
            temp_max = weathermath.kelvin_to_celcius( self.weather['main']['temp_max'])
            pressure = self.weather['main']['pressure']
            humidity = self.weather['main']['humidity']
            desc = self.weather['weather'][0]['description']
            clouds = self.weather['clouds']['all']
            wind_speed = weathermath.ms_to_mph(self.weather['wind']['speed'])
            wind_deg = weathermath.deg_to_cardinal(self.weather['wind']['deg'])
            sunrise = datetime.datetime.utcfromtimestamp(self.weather['sys']['sunrise']).strftime('%H:%M:%S')
            sunset = datetime.datetime.utcfromtimestamp(self.weather['sys']['sunset']).strftime('%H:%M:%S')
            station_name = self.weather['name']

            print ("\nStation Name: %s\n%s\nDescription: %s\nSunrise: %s\nSunset: %s\nTemp: %.2fc\nMin Temp: %.2fc\nMax Temp: %.2fc\nPressure: %.2fhPa\nHumidity: %.2f%%\nClouds: %.2f%%\nWind Speed: %.2fmph\nWind Deg: %s"
                    % (station_name, timestamp, desc, sunrise, sunset, temp, temp_min, temp_max, pressure, humidity, clouds, wind_speed, wind_deg))
