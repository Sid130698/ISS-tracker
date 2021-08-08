import requests #makes requests to api
from datetime import datetime
import smtplib
import time



BOT_EMAIL="thepythonbot1306@gmail.com"
BOT_PASSWORD='sid130698'
MY_LAT,MY_LNG=13.129650577714324, 77.58757345531257

def is_iss_overhead():
    response=requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data=response.json()
    iss_position=data['iss_position']
    longitude=float(iss_position['longitude'])
    latitude=float(iss_position['latitude'])
    if (MY_LAT + 5==latitude or MY_LAT-5==latitude ) and (MY_LNG+5==longitude or MY_LNG-5==longitude):
        return True
    return False
# iss_position=(longitude,latitude)
# print(iss_position)
def is_night():
    parameters={
        "lat":MY_LAT,
        "lng":MY_LNG,
        "formatted":0
    }


    response=requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data=response.json()
    sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset=int(data['results']['sunset'].split("T")[1].split(":")[0])



    print(sunrise)
    print(sunset)


    time_now=datetime.now()
    my_hour=time_now.hour
    if my_hour-5<0:
        my_hour=my_hour+24-5
    if my_hour>=sunset or my_hour<=sunrise :
        return True
    return False

def send_me_email():
    connection=smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(BOT_EMAIL,BOT_PASSWORD)
    connection.sendmail(from_addr=BOT_EMAIL,
     to_addrs='sidsingh130698@gmail.com',
     msg="Subject:Look Up👀👆☝️⬆️\n\nThe ISS🛰️🛰️🛰️🛰️ is in the sky above your location"
    )





if is_iss_overhead() and is_night():
    while True:
        time.sleep(60)
        send_me_email()
    