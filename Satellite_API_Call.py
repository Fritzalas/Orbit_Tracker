import requests

# Retrieve the future positions of any satellite as groundtrack (latitude, longitude) to display orbits on maps, and also the satellite velocity.

def get_satellites_above(id, observer_lat, observer_lng, observer_alt ,seconds, api_key):
    """
        Fetches future positions of a satellite along with azimuth and elevation with respect to the observer.

        Args:
        - norad_id (int): NORAD ID of the satellite.
        - observer_lat (float): Observer's latitude in decimal degrees.
        - observer_lng (float): Observer's longitude in decimal degrees.
        - observer_alt (float): Observer's altitude in meters.
        - seconds (int): Number of seconds into the future to retrieve positions.
        - api_key (str): N2YO API key.

        Returns:
        - list: A list of satellite positions and angles, or an error message.
        """

    # Define the API endpoint
    url = f'https://api.n2yo.com/rest/v1/satellite/positions/{id}/{observer_lat}/{observer_lng}/{observer_alt}/{seconds}/&apiKey={api_key}'
    try:
        # Make the API request
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # Return the list of future positions
            return data['positions']
        else:
            return f"Error: {response.status_code} - {response.text}"

    except Exception as e:
        return f"An error occurred: {str(e)}"