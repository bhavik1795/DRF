import requests
import json

'''    Serialization'''
# URL = "http://localhost:8000/stuinfo/3" 

# r = requests.get(url=URL)
# data = r.json()
# print(data)


'''     Deserialization'''

URL = "http://localhost:8000/stucreate/"

data = {
    'name' : 'Viraj',
    'roll' : '22',
    'city' : 'Borivali'
}

json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data) 
data = r.json()
print(data)
