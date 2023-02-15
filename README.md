# MyWeatherBot
Hello, here is a telegram bot that can send weather.
There are two ways to check the current weather:
* Submit your location (button: Submit your location 📍)
* Write the name of your locality

## To start the bot you need:
1. Install MongoDB
2. Create configuration file "config.ini" with the following format:
```
[APIKEY]
APIKEY_BOT = ...

[DB_KEY]
HOST = ...
PORT = ...
```
3. Install virtual environment and configure dependencies:
```
pip install -r requirements.txt
```
