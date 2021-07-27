import urllib.request
import json
import os 
from dotenv import load_dotenv

load_dotenv()
offset = 1
number = 0
header = {'token': os.environ['apitoken']}

for i in range(39):
    url = f'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?offset={offset}&limit=1000'
    request = urllib.request.Request(url ,headers=header)
    with urllib.request.urlopen(request) as f:
        #string = f.read().decode('utf-8')
        object = json.loads(f.read())
        with open (f'json_data/locations_{number}.json', 'w') as f:
            json.dump(object, f)
    number += 1
    offset += 1000

