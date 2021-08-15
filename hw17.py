#!/usr/bin/python
#pip install GPSPhoto

from GPSPhoto import gpsphoto
data=gpsphoto.getGPSData("hw17.jpg")
file=open("hw16.txt", "w")
file.write(f"{str(data['Latitude'])},{str(data['Longitude'])}")
file.close()







