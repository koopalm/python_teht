# import urllib library
from urllib.request import urlopen
import json


my_list = []
for data in range(5):
    url = "https://catfact.ninja/fact"
    response = urlopen(url)
    data_json = json.loads(response.read())
    my_list.append(data_json)

for item in my_list:
    print(item)