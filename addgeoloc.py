#!/usr/bin/env python

from csv import reader, writer
import googlemaps

GMAPS_KEY = CONFIG['gmaps_api_key']
gmaps = googlemaps.Client(key=GMAPS_KEY)


def get_lon_lat(addr):
    geocode_result = gmaps.geocode(addr)
    return geocode_result[0]['geometry']['location']

kg_info_with_pos = []
with open('kinderextract.csv', newline='') as f:
    kg_info = reader(f, delimiter=';')
    # skip the header line
    next(kg_info)
    for r in kg_info:
        kg_pos = get_lon_lat(r[3])
        kg_info_with_pos.append(r + kg_pos['lng'] + ';' + kg_pos['lat'] + ';')
with open('geo_kindergarteninfo.csv', 'w') as f:
    kg_geo_info = writer(f)
    kg_geo_info.writerows(kg_info_with_pos)
