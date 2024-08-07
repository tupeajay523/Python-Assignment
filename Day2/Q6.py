"""Q6. Write a Python program that write data in csv file using pandas of ISS Location with timestamp min 100 records 
Use this url to get the data of ISS 
(Url: http://api.open-notify.org/iss-now.json) """



import requests
import pandas as pd
from datetime import datetime

url = 'http://api.open-notify.org/iss-now.json'

data_list = []

for _ in range(100):
    response = requests.get(url)
    data = response.json()
    
    data_list.append({
        'timestamp': datetime.fromtimestamp(data['timestamp']),
        'latitude': data['iss_position']['latitude'],
        'longitude': data['iss_position']['longitude']
    })

df = pd.DataFrame(data_list)

df.to_csv('iss_location.csv', index=False)

print("Data written to 'iss_location.csv'")