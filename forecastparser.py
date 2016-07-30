import weathermath, datetime

class ForecastParser:

    def __init__(self, forecast, count):
        self.forecast = forecast
        self.count = count
        self.dts = []
        self.temps = []
        self.temps_min = []
        self.temps_max = []
        self.pressures = []
        self.humidities = []
        self.descriptions = []
        self.clouds = []
        self.wind_speeds = []
        self.wind_degs = []
        self.__parse_forecast()

    def __parse_forecast(self):
        for i in range(self.count):
            if i >= self.forecast['cnt']:
                break

            self.dts.append(self.forecast['list'][i]['dt'])
            self.temps.append(self.forecast['list'][i]['main']['temp'])
            self.temps_min.append(self.forecast['list'][i]['main']['temp_min'])
            self.temps_max.append(self.forecast['list'][i]['main']['temp_max'])
            self.pressures.append(self.forecast['list'][i]['main']['pressure'])
            self.humidities.append(self.forecast['list'][i]['main']['humidity'])
            self.descriptions.append(self.forecast['list'][i]['weather'][0]['description'])
            self.clouds.append(self.forecast['list'][i]['clouds']['all'])
            self.wind_speeds.append(self.forecast['list'][i]['wind']['speed'])
            self.wind_degs.append(self.forecast['list'][i]['wind']['deg'])

    def display(self):
        for i, _e in enumerate(self.dts):
            print("%d days and %d hours ahead" %(((i+1)*3)/24 ,((i+1)*3)%24))
            timestamp = datetime.datetime.utcfromtimestamp(self.dts[i]).strftime('%d-%m-%Y %H:%M:%S')
            temp = weathermath.kelvin_to_celcius(self.temps[i])
            temp_min = weathermath.kelvin_to_celcius(self.temps_min[i])
            temp_max = weathermath.kelvin_to_celcius(self.temps_max[i])
            pressure = self.pressures[i]
            humidity = self.humidities[i]
            desc = self.descriptions[i]
            clouds = self.clouds[i]
            wind_speed = weathermath.ms_to_mph(self.wind_speeds[i])
            wind_deg = weathermath.deg_to_cardinal(self.wind_degs[i])

            print ("%s\nDescription: %s\nTemp: %.2fc\nMin Temp: %.2fc\nMax Temp: %.2fc\nPressure: %.2fhPa\nHumidity: %.2f%%\nClouds: %.2f%%\nWind Speed: %.2fmph\nWind Deg: %s\n"
                    % (timestamp, desc, temp, temp_min, temp_max, pressure, humidity, clouds, wind_speed, wind_deg))
