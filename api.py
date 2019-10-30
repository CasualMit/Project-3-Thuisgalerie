import requests
import pprint

def api_request(key):
    apikey = 'oh7gzUCb'
    apiurl = 'https://www.rijksmuseum.nl/api/nl/collection'
    params = dict(key=apikey, format='json')
    url = apiurl
    request = requests.get(url, params=params)
    res = request.json()
    return res[key]


def api_filter(key):
    test = api_request(key)
    new_format = dict()
    for item in test:
        art_data = dict()
        # pprint.pprint(item)
        # pprint.pprint(item['id'])
        # pprint.pprint(item['title'])
        # pprint.pprint(item['webImage']['url'])
        # pprint.pprint(item['principalOrFirstMaker'])

        art_data['titel'] = item['title']
        art_data['artiest'] = item['principalOrFirstMaker']
        art_data['image'] = item['webImage']['url']
        new_format[item['id']] = art_data
    pprint.pprint(new_format)

    return

api_filter('artObjects')

# test = '/SK-C-5'