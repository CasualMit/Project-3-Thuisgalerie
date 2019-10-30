import requests
import json
import pprint

# apikey = 'oh7gzUCb'
# apiurl = 'https://www.rijksmuseum.nl/api/nl/collection/SK-C-5?'
# params = dict(key=apikey, format=json)
# request = requests.get(apiurl, params=params)

request = requests.get('https://www.rijksmuseum.nl/api/nl/collection/?key=oh7gzUCb&format=json')
data = request.json()
pprint.pprint(data)
