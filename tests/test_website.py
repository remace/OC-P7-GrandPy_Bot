import requests
from tests import constants


class Test_Views:

    def setup_method(self):
        self.params = {
            'sentence': 'connais tu le palais idéal du facteur cheval?'
        }

    def test_grandpy_api(self):
        result = {'maps_info': constants.USEFUL_DATA,
                  'wiki_info': constants.WIKIPEDIA_INTRO}
        rep = requests.get('http://127.0.0.1:5000/AskGrandpy/', self.params).json()
        assert rep == result
