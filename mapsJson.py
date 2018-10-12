import googlemaps
import pdb
import json
import time


def get_best_restaurant(rests):
    if not rests:
        return None

    buf=rests[0]

    for res in rests:
        if 'rating' in res and res['rating'] > buf['rating']:
                buf = res

    return buf



if __name__ == '__main__':
    gmaps = googlemaps.Client(key='AIzaSyDmECqKm1tLn3NggSC-WdsAmpchRyT1bWY')
    result = gmaps.geocode('Ukraine, Sumy')

    # pdb.set_trace()

    loc = result[0]['geometry']['location']
    pl = gmaps.places_nearby(loc, 5000, type='restaurant')
    #time.sleep(2)

    best = get_best_restaurant(pl['results'])
    print(best['name'] + ' ' + str(best['rating']))

    # вывод всего списка имен
    # n=0
    # while n<=(len(pl['results'])-1):
    #     print(str(n+1)+'.'+pl['results'][n]['name']+' '+str(pl['results'][n]['rating']))
    #     n+=1
