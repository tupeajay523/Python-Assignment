"""
Q3 Write a Python program that reads a JSON file containing NASA APOD data and prints the keys: "explanation","Title" 
Use this link to copy your json data (do not use request module, just save the Json to a variable then do json operation) 
JSON Data url: https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY 

"""


import json


json_data = '''
{
  "date": "2023-08-01",
  "explanation": "Explanation of the APOD image or video for the day.",
  "hdurl": "https://apod.nasa.gov/apod/image/2308/APODimage.jpg",
  "media_type": "image",
  "service_version": "v1",
  "title": "Title of the APOD for the day",
  "url": "https://apod.nasa.gov/apod/image/2308/APODimage.jpg"
}
'''


data = json.loads(json_data)


explanation = data.get("explanation")
title = data.get("title")

print("Explanation:", explanation)
print("Title:", title)
