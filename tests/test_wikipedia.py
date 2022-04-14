from libs.API import wikipedia_API
from tests import constants
import requests
from io import BytesIO
import json


def mocked_requests_get(json_data, status_code, *args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    return MockResponse(json_data, status_code)


class Test_Wikipedia_API:
    def setup_method(self):
        self.w = wikipedia_API.Wikipedia_API()

    def teardown_method(self):
        self.w = None

    def test_get_pages_around_location(self, monkeypatch):
        result = {
            "wikipedia_infos": constants.JSON_WIKIPEDIA_RESPONSE_GEOSEARCH,
            "status": "OK",
        }

        def mock_return(*args, **kwargs):
            results = constants.JSON_WIKIPEDIA_RESPONSE_GEOSEARCH
            response = mocked_requests_get(json_data=results, status_code=200)
            return response

        monkeypatch.setattr(requests, "get", mock_return)
        assert (
            self.w._get_pages_around_location(lat=45.25653760000001, lng=5.0282228)
            == result
        )

    def test_select_best_page(self, monkeypatch):
        result = constants.JSON_WIKIPEDIA_RESPONSE_GEOSEARCH["query"]["geosearch"][0]

        def mock_return(*args, **kwargs):
            results = constants.JSON_WIKIPEDIA_RESPONSE_GEOSEARCH
            response = mocked_requests_get(json_data=results, status_code=200)
            return response

        monkeypatch.setattr(requests, "get", mock_return)

        self.w._get_pages_around_location(lat=45.25653760000001, lng=5.0282228)
        assert self.w._select_best_page("connais palais idéal facteur cheval") == result

    def test_select_best_page_void_response(self):
        result = []
        self.w._get_pages_around_location(lat=45.25653760000001, lng=5.0282228)
        assert self.w._select_best_page("miizefvduhb^paeqiubfvùâebufùOanue") == result

    def test_get_introduction(self):
        result = {
            "title": constants.WIKIPEDIA_INTRO["query"]["pages"]["332154"]["title"],
            "intro": constants.WIKIPEDIA_INTRO["query"]["pages"]["332154"]["extract"],
        }
        self.w._get_pages_around_location(lat=45.25653760000001, lng=5.0282228)
        self.w._select_best_page("connais palais idéal facteur cheval")
        assert self.w._get_infos_on_page() == result

    def test_search_wikipedia(self):
        result = {
            "wikipedia_infos": {
                "info": {
                    "title": constants.WIKIPEDIA_INTRO["query"]["pages"]["332154"][
                        "title"
                    ],
                    "intro": constants.WIKIPEDIA_INTRO["query"]["pages"]["332154"][
                        "extract"
                    ],
                },
                "status": "OK",
            },
        }
        assert (
            self.w.search_wikipedia(
                lat=45.25653760000001,
                lng=5.0282228,
                sentence="connais palais idéal facteur cheval",
            )
            == result
        )
