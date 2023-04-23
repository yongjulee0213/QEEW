'''
📌history
0423 : 모듈화, 파일이름 변경 -> get_lat_lng
'''
import requests
import googlemaps
import json
from geopy.geocoders import Nominatim

def get_lat_lng():

    GOOGLE_API_KEY="AIzaSyAK7mtHLoSolHqlJnWI3yk5nw3BOiLyu1w"

    url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={GOOGLE_API_KEY}'
    data = {
        'considerIp': True, # 현 IP로 데이터 추출
    }

    result = requests.post(url, data) # 해당 API에 요청을 보내며 데이터를 추출한다.

    #print(result.text)
    result2 = json.loads(result.text)

    lat = result2["location"]["lat"] # 현재 위치의 위도 추출
    lng = result2["location"]["lng"] # 현재 위치의 경도 추출

    #0423: 여기를 가져오면된다!!!!!----------------
    print('------get_lat_lng------')
    print('lat: ', lat)#위도
    print('lng: ', lng)#경도
    #--------------------------------------
    return lat, lng