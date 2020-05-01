import certifi
import ssl
import geopy
import math
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import numpy as np
ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx



def generateData(reqData):
  # initialize
  data = {"demands": [], "location_ids": [], "depot": 0}
  geolocator = Nominatim(user_agent="my-droptimize")

  # get geopy obj
  points = [];
  totalQty = 0
  points.append(geolocator.geocode(reqData['depot']['address']))
  data["demands"].append(0)
  data["location_ids"].append(reqData['depot']['location_id'])
  for delivery in reqData['deliveries']:
    points.append(geolocator.geocode(delivery['address']))
    data["demands"].append(delivery['quantity'])
    data["location_ids"].append(delivery ['location_id'])
    totalQty += delivery['quantity']
  
  # debug
  for point in points:
    print(point.address)

  # generate distance matrix
  dist = lambda p1, p2: geodesic((p1.latitude, p1.longitude), (p2.latitude, p2.longitude)).km
  data['distance_matrix'] = np.asarray([[dist(p1, p2) for p2 in points] for p1 in points])

  # calculate rest of the fields
  data["num_vehicles"] = math.ceil(totalQty / reqData['depot']['vehicle_capacity'])
  data["vehicle_capacities"] = [reqData['depot']['vehicle_capacity']] * data["num_vehicles"]

  # return
  print(data)
  return data
