from tests import constants
from GrandPy import GrandPy

class Test_Grandpy:

    def msetup_method(self):
        result={'maps_info': constants.USEFUL_DATA,
                'wiki_info': constants.WIKIPEDIA_INTRO}
        gp = GrandPy.GrandPy()
        assert gp.answer("connais-tu le palais idéal du facteur cheval?") == result