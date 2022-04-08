#!/usr/bin/env python3
"""
@desc API manager for Grandpy_bot
@author Rémi "remace" Tauvel
@version 0.0.1
@date 2021-07-21
"""


from libs.API import wikipedia_API, GMapsAPI, statsAPI
from libs.parsing import parser


class GrandPy:

    def __init__(self):
        self.parser = parser.SentenceParser()
        self.google_maps = GMapsAPI.GMapsAPI()
        self.wikipedia = wikipedia_API.Wikipedia_API()
        self.stats = statsAPI.StatsAPI()
        self.response = {}

    def answer(self, sentence):
        
        clear_sentence = self.parser.get_clean_sentence(sentence)
        self.response['maps_info'] = self.google_maps.search(clear_sentence)
        if self.response['maps_info']['status'] == 'OK':
            lat = self.response['maps_info']['results']['geometry']['location']['lat']
            lng = self.response['maps_info']['results']['geometry']['location']['lng']
            self.stats.set_maps_data(self.response['maps_info'])
            self.stats.register_query()
            wiki = self.wikipedia.search_wikipedia(lat, lng, clear_sentence)['wikipedia_infos']
            if wiki['status'] == 'OK':
                self.response['status'] = 'OK'
                self.response['wiki_info'] = wiki
                return self.response
            else:
                self.response['status'] = 'ZERO_RESULTS_WIKI'
                self.response['message'] = "j'ai l'impression que c'est là. essaye de me dire dans quelle ville ça se " \
                                      "trouve dans ta question"
                return self.response
            
        else:
            self.response = {
                'status': 'ZERO_RESULTS_GMAPS',
                'message': "je ne connais pas cet endroit. peut-être tu peux essayer d'être plus précis?"
            }

            return self.response
