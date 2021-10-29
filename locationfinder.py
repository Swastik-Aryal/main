import json
import requests



ipadress ="209.85.220.41"
api_request = requests.get("http://www.geoplugin.net/json.gp?ip=ipadress")
my_api = json.loads(api_request.content)
print (str(my_api))