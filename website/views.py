#!/usr/bin/env python3
"""
@desc website
@author Rémi "remace" Tauvel
@version 0.0.1
@date 2021-07-14
"""

from flask import Flask, render_template, request
from GrandPy import GrandPy
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/AskGrandPy/', methods=['POST', 'GET'])
def AskGrandPy():
    if request.method == 'POST':
        sentence = request.form['sentence']
    elif request.method == 'GET':
        sentence = request.args.get('sentence')
    else:
        return {"error": "bad method"}
    grandpy = GrandPy.GrandPy()
    return grandpy.answer(sentence), 200


if __name__ == "__main__":
    app.run(debug=True)
