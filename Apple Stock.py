import urllib
import json
import requests

#AirPods MMEF2AM/A

def get_status(name, partnum, zipcode):
	print("==========================================")
	print ("Checking "  + name + " " + zipcode)
	print("==========================================")
	
	url = "http://www.apple.com/shop/retail/pickup-message?parts.0=" + (partnum) + "&location=" + zipcode
	
	r = requests.get(url)
	json = r.json()
	
	body = json['body']
	
	for store in body['stores']:
		status = store['partsAvailability']
		print (store['storeName'].ljust(20) + ": " + str(status[partnum]['pickupDisplay']).rjust(20))

get_status("AirPods",  "MMEF2AM/A", "98112")
get_status("Series 4 Black Stainless Sport",  "MTV52LL/A", "98112")
get_status("Series 4 Black Stainless Milanese",  "MTV62LL/A", "98112")
