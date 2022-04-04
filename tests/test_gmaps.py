from libs.API import GMapsAPI
from tests import constants
import requests
from io import BytesIO
import json


class Test_GMapsAPI:

    def setup_method(self):
        self.gm = GMapsAPI.GMapsAPI()

    def teardown_method(self):
        self.gm = None

    def test_get_location(self, monkeypatch):
        results = constants.GMAPS_ANSWER
        
        def mock_return(*args, **kwargs):
            results = constants.GMAPS_ANSWER
            return BytesIO(json.dumps(results).encode())

        monkeypatch.setattr(requests, 'get', mock_return)

        assert self.gm._get_location("connais palais idéal facteur cheval") == results

    def test_get_location_not_existing(self, monkeypatch):
        results = constants.GMAPS_ANSWER_ZERO_RESULT
        def mock_return(*args, **kwargs):
            results = constants.GMAPS_ANSWER_ZERO_RESULT
            return BytesIO(json.dumps(results).encode())

        monkeypatch.setattr(requests, 'get', mock_return)
        assert self.gm._get_location('pmquhvb^quehgtbùôquetngùO') == results

    def test_get_useful_data_from_response(self, monkeypatch):
        results = constants.USEFUL_DATA
        def mock_return(*args, **kwargs):
            results = constants.USEFUL_DATA
            return BytesIO(json.dumps(results).encode())

        monkeypatch.setattr(requests, 'get', mock_return)

        self.gm._get_location("connais palais facteur cheval")
        assert self.gm._get_useful_data_from_response() == constants.USEFUL_DATA

    def test_search(self, monkeypatch):

        results = constants.USEFUL_DATA

        def mock_return(*args, **kwargs):
            search_result = constants.USEFUL_DATA
            return BytesIO(json.dumps(search_result).encode())

        monkeypatch.setattr(requests, 'get', mock_return)


        assert self.gm.search("connais palais facteur cheval") == results
