import weatherparser, forecastparser, webreader, weathermath, location

def main():
    request_location()
    loc.display()
    weather_query()
    forecast_query()

def request_location():
    print("Enter location name.")
    name = input().lower().strip()
    wr = webreader.WebReader(name)
    global loc
    loc = location.Location(name, wr.lat, wr.lng, wr.altitude, wr.weather, wr.forecast) # global to module only?

def weather_query():
    if read_input("Would you like to display the weather?[Y/n]"):
        weatherparser.WeatherParser(loc.weather).display()

def forecast_query():
    if read_input("Would you like to display the 12h forecast?[Y/n]"):
        forecastparser.ForecastParser(loc.forecast, 4).display()
    if read_input("Would you like to display the full forecast?[Y/n]"):
        forecastparser.ForecastParser(loc.forecast, 100).display()

def read_input(prompt):
    yes = set(['yes','y', 'ye'])
    print(prompt)

    if input().lower().strip() in yes:
        return True
    else:
        return False

main()
