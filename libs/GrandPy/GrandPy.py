#!/usr/bin/env python3
"""
@desc API manager for Grandpy_bot
@author Rémi "remace" Tauvel
@version 0.0.1
@date 2021-07-21
"""


from libs.API import wikipedia_API, GMapsAPI
from libs.parsing import parser


class GrandPy:

    def __init__(self):
        self.parser = parser.SentenceParser()
        self.google_maps = GMapsAPI.GMapsAPI()
        self.wikipedia = wikipedia_API.Wikipedia_API()

    def answer(self, sentence):
        response = {}
        clear_sentence = self.parser.get_clean_sentence(sentence)
        response['maps_info'] = self.google_maps.search(clear_sentence)
        lat = response['maps_info']['results']['geometry']['location']['lat']
        lng = response['maps_info']['results']['geometry']['location']['lng']
        response['wiki_info'] = self.wikipedia.search_wikipedia(lat, lng, clear_sentence)
        return response
