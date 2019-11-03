import requests
import json
import os
import time


def api_request(key):
    """
        Function to only cache a specific key of api request will create a cache.txt with JSON.
        optional keys:
        countFacets
        artObjects
        facets
    """
    apikey = 'oh7gzUCb'
    apiurl = 'https://www.rijksmuseum.nl/api/nl/collection'
    params = dict(key=apikey, ps=4, format='json')  # ps defines the amount of results
    request = requests.get(apiurl, params=params)
    res = request.json()
    pieces = res[key]
    with open('cache.txt', 'w') as outfile:
        json.dump(pieces, outfile)


def check_cache(filename, key='artObjects'):
    """ check if the cache is older than an hour to prevent too many api calls.
     returns True or False.
     If no cache is present it will request one. """
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


def maintain_items():
    """ This function will make sure to keep items that are reserved reserved.
    And will remove the reserved items from the file available.txt """

    with open('cache.txt') as json_file:
        cache = json.load(json_file)

    reserved = check_reservedfile()

    for key, value in reserved.items():
        kunst_id = value
        for key in kunst_id:
            kunst_id = key

    reserved_art_pieces = set()
    for reserved_item in reserved:
        if kunst_id in cache:
            reserved_art_pieces.add(kunst_id)

    available_art_pieces = dict()
    for item in cache:
        if item not in reserved_art_pieces and item != 'formatted':
            available_art_pieces[item] = cache[item]
    with open('available.txt', 'w') as outfile:
        json.dump(available_art_pieces, outfile)


def check_reservedfile():
    """ Here is checked if reserved.txt exists this is needed in the keep_reserved function """
    while True:
        if os.path.isfile('reserved.txt'):
            with open('reserved.txt') as json_file:
                reserved = json.load(json_file)
            return reserved
        else:
            empty_json = dict()
            with open('reserved.txt', 'w') as outfile:
                json.dump(empty_json, outfile)


def request(objects):
    """ This is the request our program will need to have all the files necessary
    """
    check = check_cache('cache.txt')
    while check:
        with open('cache.txt') as json_file:
            cache = json.load(json_file)
        if type(cache) is dict and cache.get('formatted') is not None:
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
            continue
    while not check:
        api_request(objects)
        request('artObjects')
        break


request('artObjects')
maintain_items()
