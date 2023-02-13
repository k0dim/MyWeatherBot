from dataclasses import dataclass
from App.database.db_settings import DBweather


@dataclass(slots=True, frozen=True)
class Coordinates:
    latitudes: float
    longitudes: float

def get_coordinates(id) -> Coordinates:
    data = DBweather().search_user(id)
    latitude = data['latitude']
    longitude = data['longitude']
    return Coordinates(latitudes=latitude, longitudes=longitude)
