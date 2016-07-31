"""
Each station returns different types and numbers of data.
This means trying to access specific atmospheric features such as wind speed or temperature
may result in a KeyError as the weather station may not provide that feature.
Therefore this module prints all information provided from each station.
"""

def display(stations):
    print("\nStations: \n")
    for item in stations:
        recursive_print(item)
        print("\n")

def recursive_print(item):
    for key, value in item.items():
        if (isinstance(value, dict)):
            recursive_print(value)
        else:
            print("%s: %s" %(key, value))
