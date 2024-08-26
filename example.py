# Example usage:
from City_Coordinates import get_city_coordinates
from City_Elevation import get_city_elevation
from Satellite_API_Call import get_satellites_info, get_satellites_above
from Submit import get_user_input
from display_satellites import create_satellite_gui

api_key = 'WAZM2J-MJM3EL-MDVLM4-5BQS'
id = 25544  # ISS NORAD ID
observer_lat = 37.9838  # Athens latitude
observer_lng = 23.7275  # Athens longitude
observer_alt = 0  # Ground level in meters
seconds = 1 # Retrieve positions for 300 seconds
search_radius = 90  # Search radius in degrees
category_id = 0  # All categories

positions = get_satellites_info(id, observer_lat, observer_lng, observer_alt, seconds, api_key)
satellites = get_satellites_above(observer_lat, observer_lng, observer_alt, search_radius, category_id, api_key)
city_coordinates = get_city_coordinates("Athens","USA")
city_elevation = get_city_elevation(37.9838,23.7275)
city, country, angle = get_user_input()
create_satellite_gui(satellites)

#print(positions)
#print(satellites)
#print(city_coordinates)
#print(city_elevation)
#print(f"City: {city}\nCountry: {country}\nAngle: {angle}°")
#print(extract_satellite_info(satellites))