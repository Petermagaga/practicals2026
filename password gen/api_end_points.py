MY_LAT=-1.478911
MY_LONG=36.956780
MY_EMAIL="ptr@gmail.com"
MY_PASSWORD="12345678"

import datetime
import requests
import smtplib
import time

def is_iss_overhead():
    response=requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data=response.json()
    print(data['iss_position'])
    iss_longitude=float((data['iss_position']['longitude']))
    iss_latitude=float((data['iss_position']['latitude']))

    iss_position=(iss_longitude,iss_latitude)

    print(iss_position)

    if MY_LONG-5<=iss_longitude<=MY_LONG+5 and MY_LAT-5<=iss_latitude<=MY_LAT+5:
        return True




def sunset_tym():
    parameters= {
        "lat":MY_LAT,
        "lng":MY_LONG,
        "formatted":0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data=response.json()
    sunrise=data['results']['sunrise']
    sunset=data['results']['sunset']

    hrs_sunset=int(sunset.split("T")[1].split(":")[0])
    hrs_sunrise=int(sunrise.split("T")[1].split(":")[0])

    print(f"sunrise {hrs_sunrise}, \n sunset {hrs_sunset}")
    time_now = datetime.datetime.now().hour

    if time_now>=hrs_sunset and time_now<=hrs_sunrise:
        return True


if is_iss_overhead() and sunset_tym():
    connection=smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_EMAIL,MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="Subject:Look Up \n\n The ISS is above you in the sky"
    )
