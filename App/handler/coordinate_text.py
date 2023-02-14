from geopy.geocoders import Nominatim


def get_coordinat(adress):
    geolocator = Nominatim(user_agent='Tests')
    location = geolocator.geocode(adress)
    
    return {
        "latitude":location.latitude, "longitude":location.longitude
    }
