from collections import OrderedDict

from API import GMapsAPI
from tests import constants
import urllib.request
from io import BytesIO
import json
from unittest import TestCase


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

        TestCase().assertDictEqual(self.gm.get_location("connais palais idéal facteur cheval"), results)

    def test_get_useful_data_from_response(self):
        self.gm.get_location("connais palais facteur cheval")
        assert self.gm.get_useful_data_from_response() == constants.USEFUL_DATA
