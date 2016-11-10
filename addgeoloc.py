#!/usr/bin/env python

from csv import reader
import googlemaps
import json

with open('config.json', 'r') as f:
    config = json.load(f)
GMAPS_KEY = config['gmaps_api_key']
gmaps = googlemaps.Client(key=GMAPS_KEY)


def get_lon_lat(addr):
    geocode_result = gmaps.geocode(addr)
    return geocode_result[0]['geometry']['location']

kg_info_with_pos = []
with open('rawdata/kinderextract.csv', newline='') as f:
    kg_info = reader(f, delimiter=';')
    # skip the header line
    next(kg_info)
    for r in kg_info:
        kg_pos = get_lon_lat(r[3])
        new_r = str(
                ';'.join(r) +
                str(kg_pos['lng']) + ';' +
                str(kg_pos['lat']) + ';'
                )
        kg_info_with_pos.append(new_r)
        print(kg_info_with_pos[-1])
with open('geo_kindergarteninfo.csv', 'w') as f:
    for i in kg_info_with_pos:
        f.write(i + "\n")
