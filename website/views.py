#!/usr/bin/env python3
"""
@desc website
@author Rémi "remace" Tauvel
@version 0.0.1
@date 2021-07-14
"""

from flask import Flask, render_template, request
from libs.GrandPy import GrandPy
import config

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', google_api_key = config.GOOGLE_MAPS_KEY)


@app.route('/AskGrandPy/', methods=['POST', 'GET'])
def ask_grandpy():
    if request.method == 'POST':
        return {"error": "bad method"}
    elif request.method == 'GET':
        sentence = request.args.get('sentence')
    else:
        return {"error": "bad method"}
    grandpy = GrandPy.GrandPy()
    return grandpy.answer(sentence)


if __name__ == "__main__":
    app.run(debug=True)
