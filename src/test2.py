
"""Simple Pickup Delivery Problem (PDP)."""

from geopy.geocoders import Nominatim



def main():
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    location = geolocator.geocode("175 5th Avenue NYC")
    print(location.address)


if __name__ == '__main__':
    main()