import weatherparser, forecastparser, stationparser, webreader, weathermath, location, fileutils

def main():
    request_location()
    loc.display()
    weather_query()
    forecast_query()
    stations_query()


def request_location():
    print("Enter location name.")
    name = input().lower().strip()
    global loc
    if fileutils.file_exists(name):
        loc = fileutils.read_file(name)
    else:
        wr = webreader.WebReader(name)
        loc = location.Location(name, wr.lat, wr.lng, wr.altitude, wr.weather, wr.forecast, wr.stations)
        fileutils.save_file(loc)

def weather_query():
    if read_input("\nWould you like to display the weather?[Y/n]"):
        weatherparser.WeatherParser(loc.weather).display()

def forecast_query():
    if read_input("\nWould you like to display the 12h forecast?[Y/n]"):
        forecastparser.ForecastParser(loc.forecast, 4).display()
        if read_input("\nWould you like to save this forecast in a file?[Y/n]"):
            fileutils.write_forecast_to_file(loc, 4)
    if read_input("\nWould you like to display the 5 day forecast?[Y/n]"):
        forecastparser.ForecastParser(loc.forecast, 40).display()
        if read_input("\nWould you like to save this forecast in a file?[Y/n]"):
            fileutils.write_forecast_to_file(loc, 40)

def stations_query():
    if read_input("\nWould you like to get the weather from the nearest sations?[Y/n]"):
        stationparser.display(loc.stations)

def read_input(prompt):
    yes = set(['yes','y', 'ye'])
    print(prompt)

    if input().lower().strip() in yes:
        return True
    else:
        return False

main()
