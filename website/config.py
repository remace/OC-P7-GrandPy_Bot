#!/usr/bin/env python3
"""
@desc website
@author Rémi "remace" Tauvel
@version 0.0.1
@date 2021-07-14
"""
import os.path as path
from dotenv import load_dotenv
dotenv_path = path.join(path.dirname(__file__), '.env')  # Path to .env file
load_dotenv(dotenv_path)


PAGE_TITLE = "GrandPy Bot"
HEADER_TITLE = 'GrandPy Bot'
HEADER_SUBTITLE = 'Il connaît tous les endroits, demandez-lui!'

