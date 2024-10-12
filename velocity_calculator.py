from cmath import cos, sin, sqrt
from math import radians, atan2


def velocity(lat1,lot1,alt1,lat2,lot2,alt2):

    # Earth radius in meters
    R = 6371000

    x1=(R+alt1)*cos(radians(lat1))*cos(radians(lot1))
    x2=(R+alt2)*cos(radians(lat2))*cos(radians(lot2))
    y1=(R+alt1)*cos(radians(lat1))*sin(radians(lot1))
    y2 = (R + alt2) * cos(radians(lat2)) * sin(radians(lot2))
    z1=(R+alt1)*sin(radians(lat1))
    z2 = (R + alt2) * sin(radians(lat2))

    d =sqrt(pow((x2-x1),2) + pow((y2-y1),2) + pow((z2-z1),2))

    return d

def haversine(lat1,lot1,alt1,lat2,lot2,alt2):
    # Earth radius in meters
    R = 6371000

    # Convert latitudes and longitudes from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lot1, lat2, lot2])

    # Differences between the coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    a = a.real
    c = 2 * atan2(sqrt(a).real, sqrt(1 - a).real)

    # Distance in meters
    distance = R * c

    # Calculate the total distance considering the altitude difference
    alt_diff = abs(alt1 - alt2)
    total_distance = sqrt(distance ** 2 + alt_diff ** 2)

    return total_distance