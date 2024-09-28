from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderQuotaExceeded

def get_city_coordinates(city_name, country_name):
    geolocator = Nominatim(user_agent="Geocoder")
    result_city = f"{city_name}, {country_name}"

    try:
        location = geolocator.geocode(result_city)
        if location:
            return (location.latitude, location.longitude)
        else:
            return "Location not found"
    except GeocoderTimedOut:
        return "Geocoding service timed out"
    except GeocoderQuotaExceeded:
        return "Geocoding quota exceeded"
    except Exception as e:
        return f"An error occurred: {e}"


    #Just added a comment