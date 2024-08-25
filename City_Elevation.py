import requests

def get_city_elevation(locations):

    """
    Get the elevation of given locations using the Open-Elevation API.
    """

    url = f"https://api.open-elevation.com/api/v1/lookup?locations={locations}"
    response = requests.get(url)
    data = response.json()

    if 'results' in data:
        return data['results']
    else:
        return None