import googlemaps
import pdb
import json
import time


def sort_by_best_rating(res):
    return res.get('rating', 0)


def get_top_best_restaurant(rests, num):
    if not rests:
        return None

    assert num > 0, "Num should be a positive number"

    rests.sort(key=sort_by_best_rating, reverse=True)
    return rests[0:num]


def get_best_restaurant(rests):
    if not rests:
        return None

    return max(rests, key=sort_by_best_rating)


if __name__ == '__main__':
    gmaps = googlemaps.Client(key='AIzaSyDmECqKm1tLn3NggSC-WdsAmpchRyT1bWY')
    result = gmaps.geocode('Ukraine, Sumy')

    # pdb.set_trace()

    loc = result[0]['geometry']['location']
    pl = gmaps.places_nearby(loc, 5000, type='restaurant')
    rest_list=pl['results']

    while 'next_page_token' in pl:
        time.sleep(2)
        pl = gmaps.places_nearby(loc, 5000, type='restaurant', page_token=pl['next_page_token'])
        rest_list += pl['results']

    best = get_top_best_restaurant(rest_list, 10)
    for res in best:
        print('{1} {0}'.format(res['name'], res['rating']))
