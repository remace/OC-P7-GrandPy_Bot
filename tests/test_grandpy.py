from tests import constants
from libs.GrandPy import GrandPy


class Test_Grandpy:

    def test_answer(self):
        result = {'maps_info': constants.USEFUL_DATA,
                  'wiki_info': {
                      'status': 'OK',
                      'wikipedia_info': {
                          'intro': constants.WIKIPEDIA_INTRO["query"]['pages']['332154']['extract'],
                          'title': constants.WIKIPEDIA_INTRO["query"]['pages']['332154']['title']
                      }
                  }}
        gp = GrandPy.GrandPy()
        assert gp.answer("connais-tu le palais idéal du facteur cheval?") == result
