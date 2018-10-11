import googlemaps
import pdb
import json


def get_best_restaurant(rests):
    n = 0
    while n < len(rests):
        i = 0
        while i < len(rests):
            buf = 0
            if (i+1) < len(rests):
                if rests[i]['rating'] > rests[i+1]['rating']:
                    buf = rests[i]
                    rests[i] = rests[i+1]
                    rests[i+1] = buf
            i += 1
        n += 1
    return rests[len(rests)-1]


if __name__ == '__main__':
    gmaps = googlemaps.Client(key='AIzaSyDmECqKm1tLn3NggSC-WdsAmpchRyT1bWY')
    result = gmaps.geocode('Ukraine, Sumy')

    # pdb.set_trace()

    loc = result[0]['geometry']['location']
    pl = gmaps.places_nearby(loc, 5000, type='restaurant')

    best = get_best_restaurant(pl['results'])
    print(best['name'] + ' ' + str(best['rating']))

    # вывод всего списка имен
    # n=0
    # while n<=(len(pl['results'])-1):
    #     print(str(n+1)+'.'+pl['results'][n]['name']+' '+str(pl['results'][n]['rating']))
    #     n+=1
