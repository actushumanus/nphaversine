#from math import radians, cos, sin, asin, sqrt

import numpy as np

AVG_EARTH_RADIUS = 6371  # in km


def nphaversine(point1, point2, miles=False):
    """ Calculate the great-circle distance bewteen two points on the Earth surface.

    :input: point1 and point2 is 2-d np array of [[lat, lon]]
    
    # IF POINT1 and POINT2 SAME SHAPE
    # THEN FUNCTION RETURNS ONE TO ONE CALCULATION

    # IF ONE POINT IS SOLO AND THE OTHER IS MULITPLE
    # THEN FUNCTION RETURNS ONE TO ALL CALCULATION

    # DOESNT WORK IF BOTH ARE MULTIPLE BUT UNEQUAL SHAPE    
    

    Example: haversine((45.7597, 4.8422), (48.8567, 2.3508))

    :output: Returns the distance bewteen the two points.
    The default unit is kilometers. Miles can be returned
    if the ``miles`` parameter is set to True.

    """

#    print point1
#    print point2    
    
    # unpack latitude/longitude
    if len(point1.shape) == 1:
        point1 = np.array([point1])
    if len(point2.shape) == 1:
        point2 = np.array([point2])
    
#    print point1
#    print point2    
    point1 = np.radians(point1)
    point2 = np.radians(point2)
    
    

    # convert all latitudes/longitudes from decimal degrees to radians
#    lat1, lng1, lat2, lng2 = map(np.radians, (lat1, lng1, lat2, lng2))

    # calculate haversine
    d = np.power(np.sin((point2[:,0] - point1[:,0]) / 2) , 2) + np.cos(point1[:,0]) * np.cos(point2[:,0]) * np.power(np.sin((point2[:,1] - point1[:,1]) / 2), 2)
    h = 2 * AVG_EARTH_RADIUS * np.arcsin(np.sqrt(d))
    if miles:
        return h * 0.621371  # in miles
    else:
        return h  # in kilometers

