import requests

class Test_Views:

    def __init__(self):
        self.params={
            'sentence': 'connais tu le palais du facteur cheval?'
        }

    def test_API_Route(self):
        result = {'maps_info': constants.USEFUL_DATA,
                  'wiki_info': constants.WIKIPEDIA_INTRO}
        rep = requests.get('http://127.0.0.1:5000/AskGrandpy/', self.params).json()
        assert rep == result
