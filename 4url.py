# -*- coding: utf-8 -*-
"""
    4url
    ~~~~

    Test app

    :author: Martin Putniorz <mputniorz@gmail.com>, 2013
    :license: see LICENSE
"""
from os import environ

import requests
from flask import Flask, redirect, jsonify

app = Flask(__name__)
app.debug = True


@app.route('/<name>')
def search(name):
    name = name.replace('-', ' ')
    payload = {
        'intent': 'browse',
        'll': '49.1950602,16.6068371',
        'radius': 50000,
        'query': name,
        'limit': 3,
        'client_id': environ['FOURSQ_ID'],
        'client_secret': environ['FOURSQ_SECRET']
    }
    r = requests.get(
        'https://api.foursquare.com/v2/venues/search', params=payload)
    try:
        venue = r.json()['response']['groups'][0]['items'][0]
        return redirect(venue['canonicalUrl'])
    except IndexError:
        return jsonify(r.json())


if __name__ == '__main__':
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
