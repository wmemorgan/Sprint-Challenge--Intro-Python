# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).
class City:
  def __init__(self, name, lat, lon):
    self.name = name
    self.lat = lat
    self.lon = lon

  def __str__(self):
    return f"{self.name}, {self.lat}, {self.lon}"

import csv

cities = []

def cityreader(cities=[]):
  # TODO Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the 
  # `cities` list

  with open("cities.csv", "r") as cities_file:
    csv_reader = csv.reader(cities_file, delimiter=',')
    next(csv_reader)

    for row in csv_reader:
      cities.append(City(row[0], row[3], row[4]))
    
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
# Get latitude and longitude values from the user
coord1 = tuple(input("Enter lat1,lon1:").split(","))
coord2 = tuple(input("Enter lat2,lon2:").split(","))

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  latitudes = [float(lat1), float(lat2)]
  longitudes = [float(lon1), float(lon2)]

  # within will hold the cities that fall within the specified region
  within = []

  for city in cities:
    conditions = [float(min(latitudes)) <= float(city.lat) <= max(latitudes), min(longitudes) <= float(city.lon) <= max(longitudes)]
    if all(conditions):
      within.append(City(city.name, float(city.lat), float(city.lon)))

  return within

for city in cityreader_stretch(coord1[0], coord1[1], coord2[0], coord2[1], cities):
  print(city)
