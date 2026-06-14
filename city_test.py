from geopy.geocoders import Nominatim

city = input("Enter City Name: ")

geolocator = Nominatim(user_agent="urban_heat_ai")

location = geolocator.geocode(city)

if location:
    print(f"City: {city}")
    print(f"Latitude: {location.latitude}")
    print(f"Longitude: {location.longitude}")
else:
    print("City not found")