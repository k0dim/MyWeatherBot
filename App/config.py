APIKEY_OWM = 'c50b8eb983df6ecb1ca32440e64ab2be'

CURRENT_WEATHER_API_CALL = (
        'http://api.openweathermap.org/data/2.5/weather?'
        'lat={latitude}&lon={longitude}&'
        'appid=' + APIKEY_OWM + '&units=metric'
)