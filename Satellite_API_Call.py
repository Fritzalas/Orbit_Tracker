import requests

# Retrieve the future positions of any satellite as groundtrack (latitude, longitude) to display orbits on maps, and also the satellite velocity.

def get_satellites_info(id, observer_lat, observer_lng, observer_alt ,seconds, api_key):
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
    print(url)
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


#The "above" function will return all objects within a given search radius above observer's location. The radius (θ), expressed in degrees, is measured relative to the point in the sky directly above an observer (azimuth).

def get_satellites_above(observer_lat, observer_lng, observer_alt,search_radius,category_id,api_key):

    """
        Fetches satellites above a given location within a search radius.

        Args:
        - observer_lat (float): Observer's latitude in decimal degrees.
        - observer_lng (float): Observer's longitude in decimal degrees.
        - observer_alt (float): Observer's altitude in meters above sea level.
        - search_radius (int): Search radius in degrees (0-90).
        - category_id (int): Category ID to filter satellites (0 for all categories).
        - api_key (str): N2YO API key.

        Returns:
        - list: A list of satellites' information or an error message.
        """

    # Define the API endpoint
    url = f'https://api.n2yo.com/rest/v1/satellite/above/{observer_lat}/{observer_lng}/{observer_alt}/{search_radius}/{category_id}/&apiKey={api_key}'
    print(url)
    try:
        # Make the API request
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # Return the list of satellites
            return data['above']
        else:
            return f"Error: {response.status_code} - {response.text}"

    except Exception as e:
        return f"An error occurred: {str(e)}"