"""Utility functions related to geocoding."""

from geopy.geocoders import Nominatim

_geolocator = Nominatim(user_agent="farm_locator")


def geocode(address: str):
    """Return (lat, lng) for an address or ``None`` on failure."""
    try:
        location = _geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
    except Exception:
        pass
    return None
