#!/usr/bin/env python3
"""
@desc Gmaps API Wrapper
@author Rémi "remace" Tauvel
@version 0.0.1
@date 2021-07-19
"""
import config
import requests


class GMapsAPI:
    def __init__(self):
        self.params = {}
        self.response = {}
        self.api_url = "https://maps.googleapis.com/maps/api/geocode/json?"
        self.params['key'] = config.GOOGLE_MAPS_KEY

    def _get_location(self, sentence):
        self.params['address'] = sentence
        self.response = requests.get(self.api_url, params=self.params).json()
        return self.response

    def _get_useful_data_from_response(self):
        useful_data = {'results': {
            'name': self.response['results'][0]['address_components'][0]['long_name'],
            'formatted_address': self.response['results'][0]['formatted_address'],
            'geometry': self.response['results'][0]['geometry']
            },
            'status': 'OK'
        }
        return useful_data

    def search(self, sentence):
        self._get_location(sentence)
        return self._get_useful_data_from_response()
