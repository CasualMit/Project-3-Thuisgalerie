import requests
import pprint
import json

def api_request(key, cached=True):
    apikey = 'oh7gzUCb'
    apiurl = 'https://www.rijksmuseum.nl/api/nl/collection'
    params = dict(key=apikey, ps=2, format='json')
    request = requests.get(apiurl, params=params)
    res = request.json()
    pieces = res[key]
    with open('cache.txt', 'w') as outfile:
        json.dump(pieces, outfile)
    return


def api_filter():
    with open('cache.txt') as json_file:
        cache = json.load(json_file)
    new_format = dict()
    for item in cache:
        art_data = dict()
        art_data['titel'] = item['title']
        art_data['artiest'] = item['principalOrFirstMaker']
        art_data['image'] = item['webImage']['url']
        new_format[item['id']] = art_data
    with open('request.txt', 'w') as outfile:
        json.dump(new_format, outfile)
    return

def new_request():
    with open('cache.txt') as json_file:
        cache = json.load(json_file)
# check create date cache.txt

print(api_request('artObjects', cached=False))
print(api_filter())
