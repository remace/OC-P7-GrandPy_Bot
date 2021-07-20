from API import GMapsAPI
from tests import constants
import urllib.request
from io import BytesIO
import json


class Test_GMapsAPI:

    def setup_method(self):
        self.gm = GMapsAPI.GMapsAPI()

    def teardown_method(self):
        self.gm = None

    def test_get_location(self, monkeypatch):
        results = constants.GMAPS_ANSWER

        def mock_return():
            return BytesIO(json.dumps(results).encode())

        monkeypatch.setattr(urllib.request, 'urlopen', mock_return)

        assert self.gm._get_location("connais palais idéal facteur cheval") == results

    def test_get_useful_data_from_response(self):
        self.gm._get_location("connais palais facteur cheval")
        assert self.gm._get_useful_data_from_response() == constants.USEFUL_DATA

    def test_search(self):
        assert self.gm.search("connais palais facteur cheval") == constants.USEFUL_DATA
