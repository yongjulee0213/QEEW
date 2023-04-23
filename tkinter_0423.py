'''
변수명 저장방법:
1. btn_객체 : 버튼
2. lbl_객체 : 라벨
3. 버튼 관련 함수
'''

'''
📌
history
0423 : 날씨가져오기
'''

from tkinter import *
import QEEW.weather as weather

window=Tk()
window.geometry('1200x800')

#초기함수
def get_weather_temp():
    weather_eng, temp_C=weather.get_weather()#날씨, 온도 가져오기
    print('get_weather_temp : weather - ', weather_eng)
    
    if weather_eng=='Clouds':
        print('Clouds')
        weather_file ="Clouds.gif"
        
    elif weather_eng=='partofsun':
        print('partofsun')
        weather_file ="partofsun.gif"
        
    elif weather_eng=='Rain':
        print('rain')
        weather_file ="ranniy.gif"
        
    else:
        print('sun')
        weather_file ="sun.gif"

    return weather_file, temp_C

def btn_get_weather_temp():
    print('----🪄btn_get_weather_temp : 날씨 새로고침----')
    global changephoto

    weather_file, temp_C=get_weather_temp()#날씨 아이콘, 온도 가져오기
    changephoto=PhotoImage(file=weather_file)
    btn_weathericon.config(image=changephoto)

    lbl_temp.configure(text=f'{temp_C}℃')#바뀐 온도 출력하기
    

weather_file, temp_C=get_weather_temp()#초기날씨, 온도 가져오기

weather_icon=PhotoImage(file=weather_file)
btn_weathericon=Button(window,image=weather_icon,command=btn_get_weather_temp)
btn_weathericon.place(x=1000, y=30)
lbl_temp=Label(window, text=f'{temp_C}℃',font='HANCOMMALANGMALANG-REGULAR')
lbl_temp.place(x=1010, y=110)

#좌표 test---------------------------------------------------------------
lbl_test=Label(window, text='(0,0)', font='HANCOMMALANGMALANG-REGULAR')
lbl_test.place(x=0,y=0)

window.mainloop()
