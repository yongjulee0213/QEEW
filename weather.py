
'''
📌history
0423 : 날씨, 온도 가져오기
'''
import QEEW.get_lat_lng as get_lat_lng #lat, long가져오기
import requests
import json

def get_weather():
    apiKey = "apikey"
    lat, lng=get_lat_lng.get_lat_lng()#lat, lng값 가져옴키 값이 안에 있음.

    api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={apiKey}"

    result = json.loads(requests.get(api).text)
    '''
    result=
    {'coord': {'lon': 127.0293, 'lat': 37.7505}, 
    'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}],
    'base': 'stations',
    'main': {'temp': 293.83, 'feels_like': 292.32, 'temp_min': 293.83, 'temp_max': 296.3, 'pressure': 1021, 'humidity': 14, 'sea_level': 1021, 'grnd_level': 1013}, 'visibility': 10000, 'wind': {'speed': 3.95, 'deg': 339, 'gust': 3.88}, 'clouds': {'all': 93}, 'dt': 1682231779, 'sys': {'type': 1, 'id': 8105, 'country': 'KR', 'sunrise': 1682196412, 'sunset': 1682244807}, 'timezone': 32400, 'id': 6801953, 'name': 'Ganeung i dong', 'cod': 200}
    '''

    #0423: 가져와야할것  :weather : 'main' , 'main' : temp <-unit변경(캘빈->섭씨)
    weather=str(result['weather'][0]['main']).strip()
    temp_K=result['main']['temp']
    temp_C=round(temp_K-273.15, 1)#화씨->섭씨로 변환. 소수점 일의자리만 나타내기
    print('\n------weather------')
    print('weather:',weather)#Clouds
    print(f'temp_K: {temp_K}, temp_C:{temp_C}')

    return weather, temp_C
