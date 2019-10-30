import requests
import pprint
import json

def api_request(key):
    apikey = 'oh7gzUCb'
    apiurl = 'https://www.rijksmuseum.nl/api/nl/collection'
    params = dict(key=apikey, ps=2, format='json')
    request = requests.get(apiurl, params=params)
    res = request.json()
    pieces = res[key]
    with open('test.txt', 'w') as outfile:
        json.dump(pieces, outfile)
    return


def api_filter():
    with open('test.txt') as json_file:
        test = json.load(json_file)
    new_format = dict()
    for item in test:
        art_data = dict()
        art_data['titel'] = item['title']
        art_data['artiest'] = item['principalOrFirstMaker']
        art_data['image'] = item['webImage']['url']
        new_format[item['id']] = art_data
    with open('request.txt', 'w') as outfile:
        json.dump(new_format, outfile)
    return


print(api_request('artObjects'))
print(api_filter())
