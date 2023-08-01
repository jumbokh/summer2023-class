import base64
import requests
import json

# Replace with the actual URL
baseurl= 'http://203.145.221.230:10101'
url = baseurl+'/run/predict'  

text="新年快到了，我們去買年菜好嗎？"



# to json formate
audio_json = json.dumps({"fn_index":0,"data":[text]})

# sed header
headers = {'Content-Type': 'application/json'}

# send the request
response = requests.post(url, data=audio_json, headers=headers)

# check response
if response.status_code == 200:
    # Parse the JSON response
    json_response = json.loads(response.text)
    audiopath = json_response['data'][0]['name']
    
    # Send a GET request to download the file
    download_response = requests.get(baseurl+"/file="+audiopath)

    if download_response.status_code == 200:
        # Set the path to save the downloaded file
        save_path = 'hakka_tts.wav'  # Replace with the desired file path
        
        # Save the downloaded file
        with open(save_path, 'wb') as file:
            file.write(download_response.content)
        print(f"Download file and save to {save_path}")
    else:
        print(f"Request failed with status code: {download_response.status_code}")            
else:
    print(f"Request failed with status code: {response.status_code}")



