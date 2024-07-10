import phonenumbers
import opencage 
from test import number 

from phonenumbers import geocoder
ch_nmber = phonenumbers.parse(number)
location = geocoder.description_for_number(ch_nmber, "tr")
print(location)

from phonenumbers import carrier
service_nmber = phonenumbers.parse(number,)
print(carrier.name_for_number(service_nmber, "tr"))

