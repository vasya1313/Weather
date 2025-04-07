import requests


city = input(str('Введите город '))
url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=93f00855b8c77a06ebe3da8aedbccbc4'

weather_data = requests.get(url).json()

print(f'Температура в городе {city}: = {round(weather_data['main']['temp'])}˚C')