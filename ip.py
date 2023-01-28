import requests
import time
from plyer import notification

notification.notify(
title=f'Fetching Data',
message=f"As Soon As Data Is Available, Please Wait",
timeout=15 # seconds
)

ip_address = requests.get('https://api.ipify.org').text
term = 1
while True:
    try:
        def get_location():
            response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
            location_data = {
                "country": response.get("country_name"),
                "ip": ip_address,
                "city": response.get("city"),
                # "region": response.get("region"),
            }
            country = location_data["country"]
            ip = location_data["ip"]
            city = location_data["city"]
            location = [country, city, ip]

            return location
        notification.notify(
            title=f'Your IP : {get_location()[2]}',
            message=f'Your Location : {get_location()[1]} in {get_location()[0]}',
            timeout=10 # seconds
        )
        break
    except Exception:
        term +=1
        if (term == 4 ):
            notification.notify(
            title=f'FINISH',
            message=f"Apologize Something Wrong, 'TRY LATER'",
            timeout=10 # seconds
            )
            break
        notification.notify(
        title=f'ERROR !',
        message=f"Couldn't Find Your Location, Try Again Please Wait ({term}/3)",
        timeout=10 # seconds
        )
    time.sleep(2) # delay for 2 seconds










