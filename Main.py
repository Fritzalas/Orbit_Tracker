from City_Coordinates import get_city_coordinates
from City_Elevation import get_city_elevation
from Satellite_API_Call import get_satellites_above
from Submit import get_user_input
from display_satellites import create_satellite_gui

#Api private key:
api_key = 'WAZM2J-MJM3EL-MDVLM4-5BQS'
category_id = 0  # All categories for 0 else check the manual at :https://www.n2yo.com/api/
#Get the user input:
city, country, angle = get_user_input()
#City Coordinates:
city_coordinates = get_city_coordinates(city,country)
#City Elevation:
city_elevation = get_city_elevation(city_coordinates[0],city_coordinates[1])
city_elevation = city_elevation['elevation'][0]
#Get the list of satellites above us:
satellites = get_satellites_above(city_coordinates[0], city_coordinates[1], city_elevation, angle, category_id, api_key)
#Display the result satellite list:
create_satellite_gui(satellites,city_coordinates[0],city_coordinates[1],city_elevation)