import requests
from tests import constants

class Test_Views:

    def setup_method(self):
        self.url = "http://127.0.0.1:5000/AskGrandPy/?"
        self.params = {
            'sentence': 'connais tu le palais idéal du facteur cheval?'
        }


    def test_grandpy_api(self):

        result = {'maps_info': constants.USEFUL_DATA,
                  'wiki_info': {
                      'wikipedia_info': {
                        'intro': constants.WIKIPEDIA_INTRO["query"]['pages']['332154']['extract'],
                        'title': constants.WIKIPEDIA_INTRO["query"]['pages']['332154']['title'],
                    },
                    'status': 'OK'
                  }
                  }
        rep = requests.get(self.url, self.params).json()
        assert rep == result
