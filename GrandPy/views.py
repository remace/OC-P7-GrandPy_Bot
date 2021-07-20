#!/usr/bin/env python3
"""
@desc website
@author Rémi "remace" Tauvel
@version 0.0.1
@date 2021-07-20
"""
from flask import Flask
from API import GMapsAPI, wikipedia_API
from parsing import parser

@app.route('/')
def Ask_Grandpy():
    pass