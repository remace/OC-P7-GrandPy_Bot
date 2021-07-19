#!/usr/bin/env python3
"""
@desc website
@author Rémi "remace" Tauvel
@version 0.0.1
@date 2021-07-14
"""

from flask import Flask, render_template
import config
app = Flask(__name__)

@app.route('/')
def index():
    # page_static_data = {}
    # page_static_data["tab_title"] = config.PAGE_TITLE
    # return render_template('index.html', static= page_static_data)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
