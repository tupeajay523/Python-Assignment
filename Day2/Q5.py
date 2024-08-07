"""Q5. Write a Python program using the requests module to send a GET request to a Given Below Url API endpoint and print the 
a) latitude 
b) longitude 
c) timestamp 
(Url: http://api.open-notify.org/iss-now.json) 
"""
import requests

url = 'http://api.open-notify.org/iss-now.json'

response = requests.get(url)

data = response.json()

print("Latitude:", data['iss_position']['latitude'])
print("Longitude:", data['iss_position']['longitude'])
print("Timestamp:", data['timestamp'])