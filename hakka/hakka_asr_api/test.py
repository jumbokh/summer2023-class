import base64
import requests
import json

# Replace with the actual URL
baseurl= 'http://203.145.221.230:7004'
url = baseurl+'/run/predict'  


# load your audio file
with open('si-06-031.wav', 'rb') as file:
    audio_data = file.read()
    #encode to base64
    audio_base64 = base64.b64encode(audio_data).decode('utf-8')

audio_prefix="data:audio/wav;base64,"

# to json formate
audio_json = json.dumps({"fn_index":0,"data":[None,{'data': audio_prefix+audio_base64,"name":"audio"}]})

# sed header
headers = {'Content-Type': 'application/json'}

# send the request
response = requests.post(url, data=audio_json, headers=headers)

# check response
if response.status_code == 200:
    print(response.text)    
else:
    print(f"Request failed with status code: {response.status_code}")



