#!/usr/bin/env python3
"""
Usage: ./geocities.py [<yaml_file> | <address>]
"""
import json
import os
import sys

from geopy import geocoders
import yaml


def format_geojson_from_docs(docs):
    out = {
        'type': 'FeatureCollections',
        'features': []
    }
    for doc in docs:
        data = doc.copy()  # don't modify original for some reason
        coordinates = data.pop('coordinates')
        out['features'].append({
            'type': 'Feature',
            'properties': data,
            'geometry': {
                'type': 'Point',
                'coordinates': coordinates.split(', ')[::-1],
            },
        })
    return out


# DEPRECATED in favor of ruby version
def geojsonize(path):
    with open(path) as fp:
        docs = yaml.load_all(fp)
        # filter and load into memory so the file can be closed
        docs = [x for x in docs if 'coordinates' in x]
    data = format_geojson_from_docs(docs)
    print(json.dumps(data))


def geocode(address):
    geolocator = geocoders.Nominatim()
    location = geolocator.geocode(address)
    print(location.address)
    print('{}, {}'.format(location.latitude, location.longitude))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    path = sys.argv[1]
    if os.path.exists(path):
        geojsonize(path)
    else:
        geocode(path)
