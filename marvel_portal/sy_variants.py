#!/usr/local/bin/python3

import requests
import json

api_key = "8ef8a37c33d62efeae393fb4a7e3cd66"
api_hash = "5b8b1d5c55c55afd0b526ddad8f98c99"
api_url = "https://gateway.marvel.com:443/v1/public/creators/7190/comics?format=comic&formatType=comic&orderBy=onsaleDate&ts=1&apikey=" + api_key + "&hash=" + api_hash

response = requests.get(api_url, headers={'referer': 'localhost'})
response_json = json.loads(response.text)

totalResults = response_json['data']['total']
offsetResults = response_json['data']['offset']
limitResults = response_json['data']['limit']
print(totalResults)

for num in range(0, totalResults, limitResults):
    response = requests.get(api_url + "&offset=" + str(num), headers={'referer': 'localhost'})
    response_json = json.loads(response.text)
    for comic in response_json['data']['results']:
        for creator in comic['creators']['items']:
            if creator['name'] == "Skottie Young" and creator['role'] == "penciller (cover)":
                print(comic['title'])
