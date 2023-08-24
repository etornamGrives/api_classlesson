from geopy.distance import geodesic
from geopy.geocoders import Nominatim


#newport_ri = (41.49008, -71.312796)
#cleveland_oh = (41.499498, -81.695391)
#print(geodesic(newport_ri, cleveland_oh).miles)

def distance(first_city, second_city):
    geolocator = Nominatim(user_agent="specify")
    location = geolocator.geocode(first_city)
    location1 = geolocator.geocode(second_city)

    ty =(location.latitude,location.longitude)
    ty1 =(location1.latitude, location1.longitude)

    print(geodesic(ty,ty1).miles)

distance("ho","PARIS")