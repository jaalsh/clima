import weathermath, datetime

# 40 is max cnt... from api. as it's 5 days into future! 3 hour segments! however someone could use program with professional account and go upto 16 days ahead
class ForecastParser:

    def __init__(self, forecast, count):
        self.forecast = forecast
        self.count = count

    def display(self):
        for i, e in enumerate(self.forecast['list']):
            if i >= self.forecast['cnt'] or i >= self.count:
                break
            print("\n%d days and %d hours ahead" %(((i+1)*3)/24 ,((i+1)*3)%24))
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

            print ("%s\nDescription: %s\nTemp: %.2fc\nMin Temp: %.2fc\nMax Temp: %.2fc\nPressure: %.2fhPa\nHumidity: %.2f%%\nClouds: %.2f%%\nWind Speed: %.2fmph\nWind Deg: %s"
                    % (timestamp, desc, temp, temp_min, temp_max, pressure, humidity, clouds, wind_speed, wind_deg))
