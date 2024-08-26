from cmath import cos, sin, sqrt
from math import radians


def velocity(lat1,lot1,alt1,lat2,lot2,alt2):

    x1=(6371000+alt1)*cos(radians(lat1))*cos(radians(lot1))
    x2=(6371000+alt2)*cos(radians(lat2))*cos(radians(lot2))
    y1=(6371000+alt1)*cos(radians(lat1))*sin(radians(lot1))
    y2 = (6371000 + alt2) * cos(radians(lat2)) * sin(radians(lot2))
    z1=(6371000+alt1)*sin(radians(lat1))
    z2 = (6371000 + alt2) * sin(radians(lat2))

    d =sqrt(pow((x2-x1),2) + pow((y2-y1),2) + pow((z2-z1),2))

    return d
