# MyWeatherBot
Привет, здесь описан телеграм-бот, который умеет отправлять погоду.
Уснать текущую погоду можно двумя способами:
* Отправить свою геолокацию (кнопка: Submit your location 📍)
* Написать название своего населенного пунка

## Для запуска бота необходимо:
1. Установить MongoDB
2. Создать файл конфигурации "config.ini" по следующему формату:
```
[APIKEY]
APIKEY_BOT = ...

[DB_KEY]
HOST = ...
PORT = ...
```
3. Установить виртуальное окружение и настроить зависимости:
```
pip install -r requirements.txt
```