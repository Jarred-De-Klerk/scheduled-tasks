import requests
import smtplib
import os

MY_USERNAME = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
# parameters = {
#     "api_key" : "blabla",
#     "lat" : -30.559483,
#     "long" : 22.937506
# } <- this will not work because you're just making up your own parameter names...

parameters = {
    "lat" : -33.960758,
    "lon" : 25.620640,
    "appid" : os.environ.get("API_KEY"),
    "cnt" : 4,
}

print(parameters)
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
weather_data = response.json()
#Not using list comp!!!
# id_list = []
# for interval in range(len(weather_data["list"])):
#     weather_id = weather_data["list"][interval]["weather"][0]["id"]
#     id_list.append(weather_id)
    # if weather_id < 700:
    #     print("Bring an Umbrella!")
#print(id_list)

#Using list comp!!!
id_list_comprehension = [weather_data["list"][interval]["weather"][0]["id"] for interval in range(len(weather_data["list"]))]
will_rain = False
for id in id_list_comprehension:
    if id < 700:
        will_rain = True
if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_USERNAME,password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_USERNAME,
                            to_addrs=MY_USERNAME,
                            msg="Subject: Rain Alert \n\nMake sure to bring an umbrella with you today!")
        msg= msg.encode("utf-8")
