#!/usr/bin/env python3
"""
@desc website
@author Rémi "remace" Tauvel
@version 0.0.1
@date 2021-07-14
"""

import requests


class Wikipedia_API:
    def __init__(self):
        self.url = 'https://fr.wikipedia.org/w/api.php'
        self.params = {}
        self.response = {}
        self.best_page = {}

    def _get_pages_around_location(self, lat, lng):
        self.params={
            "action": 'query',
            'list': 'geosearch',
            'format': 'json',
            'gsradius': 1000,
            'gslimit': 10,
            'gscoord': f"{lat}|{lng}"
        }
        self.response = requests.get(self.url, self.params).json()
        return self.response

    def _select_best_page(self, sentence):
        sentence_as_list = sentence.split(' ')
        index = -1
        previous_count = 0

        for page in self.response['query']['geosearch']:
            count = 0
            index += 1
            for word in sentence_as_list:
                if word in page['title']:
                    count += 1
            if count > previous_count:
                self.best_page = page
        return self.best_page

    def _get_infos_on_page(self):
        self.params = {
            'action': 'query',
            'prop': 'extracts',
            'format': 'json',
            'exintro': 'true',
            'explaintext': 'true',
            'pageids': self.best_page['pageid']
        }

        response = requests.get(self.url, self.params).json()
        infos = {
            'title': response['query']['pages'][f'{self.best_page["pageid"]}']['title'],
            'intro': response['query']['pages'][f'{self.best_page["pageid"]}']['extract']
        }
        return infos

    def search_wikipedia(self,lat,lng,sentence):
        self._get_pages_around_location(lat=lat, lng=lng)
        self._select_best_page(sentence)
        return self._get_infos_on_page()

