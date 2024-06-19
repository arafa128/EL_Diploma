import requests
from pprint import pprint

URL = requests.get("https://api.ipify.org/?format=json")
Json_Format = dict(URL.json())
IP = str(Json_Format.get("ip"))

URL = requests.get(f"https://ipinfo.io/{IP}/geo")
pprint(URL.json())