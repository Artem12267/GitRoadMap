import requests

api_KEY = 'c6d6d8f1-d02f-489c-9b3c-1f4811a99b3d'

headers = {'X-Yandex-API-Key': api_KEY}
params = {'lat': '53.507852', 'lon': '49.420416'}
response = requests.get(f'https://api.weather.yandex.ru/v2/forecast', headers=headers, params=params)
print(response)
w = response.json()
print(w)
