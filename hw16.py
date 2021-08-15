"""
Написать программу, которая будет считывать из файла gps координаты,
и формировать текстовое описание объекта и ссылку на google maps.
Пример:

Input data: 60,01';30,19'
Output data:
Location: Теремок, Енотаевская улица, Удельная, округ Светлановское, Выборгский район, Санкт-Петербург, Северо-Западный федеральный округ, 194017, РФ
Goggle Maps URL: https://www.google.com/maps/search/?api=1&query=60.016666666666666,30.322
"""
from geopy.geocoders import Nominatim
file=open("hw16.txt", "r")
gps=file.read()
file.close()

# url="https://www.google.com/maps/search/?api=1&query="
url="https://www.google.com/maps/place/"
url=url+gps
geolocator = Nominatim(user_agent="hw16_2021")
location = geolocator.reverse(gps)
print(f"Location: {location.address}")
print(f"Goggle Maps URL: {url}")

