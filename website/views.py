#!/usr/bin/env python3
"""
@desc website
@author Rémi "remace" Tauvel
@version 0.0.1
@date 2021-07-14
"""

from flask import Flask, render_template, request
from libs.GrandPy import GrandPy
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', google_api_key = os.environ.get('GOOGLE_MAPS_KEY'))


@app.route('/AskGrandPy/', methods=['GET'])
def ask_grandpy():
    sentence = request.args.get('sentence')
    grandpy = GrandPy.GrandPy()
    return grandpy.answer(sentence)


if __name__ == "__main__":
    app.run(debug=True)
