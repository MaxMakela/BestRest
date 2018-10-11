import googlemaps
import pdb
import json

gmaps = googlemaps.Client(key='AIzaSyDmECqKm1tLn3NggSC-WdsAmpchRyT1bWY')
result = gmaps.geocode('Ukraine, Sumy')

#pdb.set_trace()

#кооридинаты
loc = result[0]['geometry']['location']
pl = gmaps.places_nearby(loc,5000,type='restaurant')
#print (json.dumps(pl['results'][0],indent=2))

n=0
while n<len(pl['results']):
    i=0
    while i<len(pl['results']):
        buf=0
        if (i+1)<len(pl['results']):
            if pl['results'][i]['rating']>pl['results'][i+1]['rating']:
                buf=pl['results'][i]['rating']
                pl['results'][i]['rating']=pl['results'][i+1]['rating']
                pl['results'][i+1]['rating']=buf
        i+=1
    n+=1

print(pl['results'][len(pl['results'])-1]['name']+' '+str(pl['results'][len(pl['results'])-1]['rating']))


"""
#вывод всего списка имен
n=0
while n<=(len(pl['results'])-1):
    print(str(n+1)+'.'+pl['results'][n]['name']+' '+str(pl['results'][n]['rating']))
    n+=1
"""
