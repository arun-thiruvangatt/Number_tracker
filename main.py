import phonenumbers
import opencage
from myphone import number
import folium

from phonenumbers import geocoder

pepnumber=phonenumbers.parse(number)

location=geocoder.description_for_number(pepnumber,"en")
print(location)

from phonenumbers import carrier

service_pro=phonenumbers.parse(number)
print(carrier.name_for_number(service_pro,"en"))

from opencage.geocoder import OpenCageGeocode

key="3205b5fe5b684a1eb65f65211650dead"

geocoder=OpenCageGeocode(key)

query=str(location)

results=geocoder.geocode(query)
# print(results)

lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']

print(lat,lng)

myMap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)

myMap.save("location.html")