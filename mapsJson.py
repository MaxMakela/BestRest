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
    rest_list=pl['results']

    if 'next_page_token' in pl:
        while 'next_page_token' in pl:
                time.sleep(2)
                #print(pl['next_page_token'])
                pl = gmaps.places_nearby(loc, 5000, type='restaurant', page_token=pl['next_page_token'])
                #print(pl)
                rest_list.append(pl['results'])

    #print(rest_list)

    print(len(rest_list))
    best = get_best_restaurant(rest_list)
    print(best['name'] + ' ' + str(best['rating']))
    # вывод всего списка имен

    #n = 0
    #while n<=(len(rest_list)-1):
    #    print(str(n+1)+'.'+rest_list[n]+' '+str(rest_list[n]['rating']))
    #    n += 1
