from tests import constants
from libs.GrandPy import GrandPy


class Test_Grandpy:

    def setup_method(self):
        self.gp = GrandPy.GrandPy()

    def teardown_method(self):
        self.gp = None

    def test_answer(self):
        result = {
            'maps_info': constants.USEFUL_DATA,
            'status': 'OK',
            'wiki_info': {
                'status': 'OK',
                'info': {
                    'intro': constants.WIKIPEDIA_INTRO["query"]['pages']['332154']['extract'],
                    'title': constants.WIKIPEDIA_INTRO["query"]['pages']['332154']['title']
                }
            }
        }
        assert self.gp.answer("connais-tu le palais idéal du facteur cheval?") == result

    def test_answer_maps_fails(self):
        result = {
            'status': 'ZERO_RESULTS_GMAPS',
            'message': "je ne connais pas cet endroit. peut-être tu peux essayer d'être plus précis?"
        }
        assert self.gp.answer("oeurtgbq^ùoqebngf ùqerdg n") == result

    def test_answer_wikipedia_fails(self):
        result = {
            'status': 'ZERO_RESULTS_WIKI',
            'maps_info': constants.USEFUL_DATA_LAUBRE,
            'message': "j'ai l'impression que c'est là. essaye de me dire dans quelle ville ça se trouve dans ta question"
        }

        assert self.gp.answer("rue de laubre") == result
