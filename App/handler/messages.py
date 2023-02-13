from App.handler.coordinat import get_coordinates
from App.handler.api_service import get_weather


def weather(user_id) -> str:
    """Returns a message about the temperature and weather description"""
    wthr = get_weather(get_coordinates(user_id))
    return f'{wthr.location}, {wthr.description}\n' \
           f'🌡 Temperature is {wthr.temperature}°C,\n' \
           f'💦 Humidity is {wthr.humidity}%\n' \
           f'Feels like {wthr.temperature_feeling}°C' \


def wind(user_id) -> str:
    """Returns a message about wind direction and speed"""
    wthr = get_weather(get_coordinates(user_id))
    return f'💨 {wthr.wind_direction} wind {wthr.wind_speed} m/s'


def sun_time(user_id) -> str:
    """Returns a message about the time of sunrise and sunset"""
    wthr = get_weather(get_coordinates(user_id))
    return f'🌄 Sunrise: {wthr.sunrise}\n' \
           f'🌅 Sunset: {wthr.sunset}\n'