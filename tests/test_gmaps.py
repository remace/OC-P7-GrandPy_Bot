from API import GMapsAPI
from tests import constants
import urllib.request
from io import BytesIO
import json
from unittest import TestCase


class Test_GMapsAPI():

    def setup_method(self):
        self.gm = GMapsAPI.GMapsAPI()

    def teardown_method(self):
        self.gm = None

    def test_http_result(self, monkeypatch):
        results = constants.gmaps_answer

        def mock_return():
            return BytesIO(json.dumps(results).encode())

        monkeypatch.setattr(urllib.request, 'urlopen', mock_return)

        TestCase().assertDictEqual(self.gm.get_location("connais palais idéal facteur cheval"), results)
