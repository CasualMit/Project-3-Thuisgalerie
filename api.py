import requests
import pprint
import json
import os
import time
# api_request('artObjects')

def api_request(key):
    apikey = 'oh7gzUCb'
    apiurl = 'https://www.rijksmuseum.nl/api/nl/collection'
    params = dict(key=apikey, ps=2, format='json')
    request = requests.get(apiurl, params=params)
    res = request.json()
    pieces = res[key]
    with open('cache.txt', 'w') as outfile:
        json.dump(pieces, outfile)


def check_cache(filename, key='artObjects'):
    # check if the cache is older than an hour to prevent too many api calls
    if os.path.isfile(filename):
        creation_time = os.path.getmtime(filename)
        now = time.time()
        age_seconds = now - creation_time
        # if the cache is older than 1 hour GET new data
        if age_seconds > 3600:
            return False
        else:
            return True
    else:
        api_request(key)


def request(objects):
    check = check_cache('cache.txt')
    while check:
        with open('cache.txt') as json_file:
            cache = json.load(json_file)
        if type(cache) is dict and cache.get('formatted') is not None:
            print('File cache.txt is ready to use!')
            break
        else:
            new_format = dict()
            for item in cache:
                art_data = dict()
                art_data['titel'] = item['title']
                art_data['artiest'] = item['principalOrFirstMaker']
                art_data['image'] = item['webImage']['url']
                new_format[item['id']] = art_data
            new_format['formatted'] = True
            with open('cache.txt', 'w') as outfile:
                json.dump(new_format, outfile)
            print('Made the request usable!')
            continue
    while not check:
        api_request(objects)
        print('Made a new request from the api!')
        request('artObjects')
        break


request('artObjects')
