#!/usr/bin/env python3
"""
@desc website
@author Rémi "remace" Tauvel
@version 0.0.1
@date 2021-07-20
"""
from flask import Flask
from API import GMapsAPI,wikipedia_API
from parsing import parser

app = Flask(__name__)

@app.route('/AskGrandpy/<sentence>/')
def ask_grandPy(sentence):
    response = {}
    p = parser.SentenceParser()
    clean_sentence = p.clean_sentence(sentence)
    gm = GMapsAPI.GMapsAPI()
    gm.get_location(clean_sentence)
    response['maps_data'] = gm.get_useful_data_from_response()

    wk = wikipedia_API.Wikipedia_API()
    wk.get_pages_around_location(lat=response['maps_data']['results']['geometry']['location']['lng'],
                                 lng=response['maps_data']['results']['geometry']['location']['lng']
                                 )
    wk.
    return maps_data

if __name__ == '__main__':
    app.run(debug=True)