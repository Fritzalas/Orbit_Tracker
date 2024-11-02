import time

from City_Coordinates import get_city_coordinates
from City_Elevation import get_city_elevation
from Satellite_API_Call import get_satellites_above, get_satellites_info
from SharedPreferences import get_preference
from Submit import get_user_input
from display_satellites import create_satellite_gui, get_satellite_data
import json
import http.server
import threading
import socketserver

from velocity_calculator import haversine

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

def update_satellite_data():
    global satellite_data
    while True:
        positions = get_satellites_info(
            get_preference("satid"),
            get_preference("observer_lat"),
            get_preference("observer_lng"),
            get_preference("observer_alt"),
            2, 'WAZM2J-MJM3EL-MDVLM4-5BQS')
        lat1 = positions[0]['satlatitude']
        lon1 = positions[0]['satlongitude']
        alt1 = positions[0]['sataltitude']
        lat2 = positions[1]['satlatitude']
        lon2 = positions[1]['satlongitude']
        alt2 = positions[1]['sataltitude']
        # Velocity:
        Converter = 3.6  # Converts the velocity to km/h

        # Velocity = velocity(lat1,lon1,alt1,lat2,lon2,alt2) * Converter
        Velocity = haversine(lat1, lon1, alt1, lat2, lon2, alt2) * Converter
        Velocity = Velocity.real

        # Format the velocity to three decimal places
        formatted_velocity = f"{Velocity:.3f}"
        satellite_data = {
            "satname": get_preference("satname"),
            "velocity": f"{formatted_velocity} km/h",
            "latitude": f"{lat2} °",
            "longitude": f"{lon2} °",
            "altitude": f"{alt2} km"
        }
        print("Updated satellite data:", satellite_data)
        time.sleep(10)


class JSONHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/satellite_data':
            # Convert current satellite data to JSON
            json_data = json.dumps(satellite_data).encode('utf-8')

            # Send response with JSON data
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_data)
        else:
            # Handle other paths (404 Not Found)
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"File not found")


# Function to start the HTTP server
def start_server():
    PORT = 8005
    with socketserver.TCPServer(("", PORT), JSONHandler) as httpd:
        print(f"Serving satellite data at: http://0.0.0.0/:{PORT}/satellite_data")
        httpd.serve_forever()

if __name__ == "__main__":
    # Start the data update function in a separate thread
    data_thread = threading.Thread(target=update_satellite_data)
    data_thread.daemon = True
    data_thread.start()

    # Start the HTTP server in a separate thread
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()

    # Keep the main program running
    while True:
        time.sleep(1)