from libs.API import GMapsAPI
from tests import constants
import requests
import json


def mocked_requests_get(json_data, status_code):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    return MockResponse(json_data, status_code)


class Test_GMapsAPI:
    def setup_method(self):
        self.gm = GMapsAPI.GMapsAPI()

    def teardown_method(self):
        self.gm = None

    def test_get_location(self, monkeypatch):
        """tests _get_location function in nominal case.
        it should return a dict describing the area found by google maps API (mocked)
        """

        def mock_return(*args, **kwargs):
            results = constants.GMAPS_ANSWER
            response = mocked_requests_get(json_data=results, status_code=200)
            return response

        monkeypatch.setattr(requests, "get", mock_return)

        assert (
            self.gm._get_location("connais palais idéal facteur cheval")
            == constants.GMAPS_ANSWER
        )

    def test_get_location_not_existing(self, monkeypatch):
        """tests _get_location function in non-nominal case.
        it should return a dict google maps API response when no result found (mocked)
        """

        def mock_return(*args, **kwargs):
            results = constants.GMAPS_ANSWER_ZERO_RESULT
            response = mocked_requests_get(json_data=results, status_code=200)
            return response

        monkeypatch.setattr(requests, "get", mock_return)
        assert (
            self.gm._get_location("pmquhvb^quehgtbùôquetngùO")
            == constants.GMAPS_ANSWER_ZERO_RESULT
        )

    def test_get_useful_data_from_response(self, monkeypatch):
        """tests _get_useful_data function
        it should return the cleaned dict with only useful data in it
        """

        def mock_return(*args, **kwargs):
            results = constants.GMAPS_ANSWER
            response = mocked_requests_get(json_data=results, status_code=200)
            return response

        monkeypatch.setattr(requests, "get", mock_return)

        self.gm._get_location("connais palais facteur cheval")
        assert self.gm._get_useful_data_from_response() == constants.USEFUL_DATA

    def test_search(self, monkeypatch):
        """tests the whole process of getting useful data from a search string.
        should return the cleaned dict with only useful data in it
        """

        def mock_return(*args, **kwargs):
            results = constants.GMAPS_ANSWER
            response = mocked_requests_get(json_data=results, status_code=200)
            return response

        monkeypatch.setattr(requests, "get", mock_return)
        assert self.gm.search("connais palais facteur cheval") == constants.USEFUL_DATA
