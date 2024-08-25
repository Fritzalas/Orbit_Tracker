import requests


def get_city_elevation(latitude, longitude):
    """
    Get the elevation of a location using the Open-Meteo API.

    Args:
        latitude (float): Latitude of the location.
        longitude (float): Longitude of the location.

    Returns:
        dict or None: A dictionary with latitude, longitude, and elevation, or None if an error occurs.
    """
    url = f"https://api.open-meteo.com/v1/elevation?latitude={latitude}&longitude={longitude}"

    try:
        response = requests.get(url)

        # Check if the response status code indicates success
        if response.status_code == 200:
            try:
                data = response.json()
            except requests.exceptions.JSONDecodeError:
                print("Error: Failed to decode JSON from the response")
                return None

            # Check if the response contains elevation data
            if 'elevation' in data:
                return data
            else:
                print("Error: 'elevation' not found in the response data")
                return None
        else:
            print(f"Error: Received status code {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to make the request due to {e}")
        return None
