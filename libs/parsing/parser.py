#!/usr/bin/env python3
"""
@parser for GrandPy Bot
@author Rémi "remace" Tauvel
@version 0.0.1
@date 2021-07-14
"""

import os
import re
import json


class SentenceParser:

    def __init__(self):
        with open(os.path.abspath(os.path.dirname(__file__)) + '/stop_words.json') as f:
            self.stop_words = json.load(f)

    def get_clean_sentence(self, sentence):
        sentence_as_table = re.split(r'\W', sentence.lower())
        clean_sentence_as_table = [word for word in sentence_as_table if word not in self.stop_words]
        clean_sentence = (" ".join(clean_sentence_as_table)).strip()
        return clean_sentence
