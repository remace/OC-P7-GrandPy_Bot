from libs.API import wikipedia_API
from tests import constants
import urllib.request
from io import BytesIO
import json


class Test_Wikipedia_API:

    def setup_method(self):
        self.w = wikipedia_API.Wikipedia_API()

    def teardown_method(self):
        self.w = None

    def test_get_pages_around_location(self, monkeypatch):
        results = constants.JSON_WIKIPEDIA_RESPONSE_GEOSEARCH
        def mock_return():
            return BytesIO(json.dumps(results).encode())
        monkeypatch.setattr(urllib.request, 'urlopen', mock_return)
        assert self.w._get_pages_around_location(lat=45.25653760000001, lng=5.0282228) == results

    def test_select_best_page(self):
        result = constants.JSON_WIKIPEDIA_RESPONSE_GEOSEARCH['query']['geosearch'][0]
        self.w._get_pages_around_location(lat=45.25653760000001, lng=5.0282228)
        assert self.w._select_best_page("connais palais idéal facteur cheval") == result

    def test_get_introduction(self):
        result = {'title': constants.WIKIPEDIA_INTRO["query"]["pages"]['332154']['title'],
                  'intro': constants.WIKIPEDIA_INTRO["query"]['pages']['332154']['extract']}
        self.w._get_pages_around_location(lat=45.25653760000001, lng=5.0282228)
        self.w._select_best_page("connais palais idéal facteur cheval")
        assert self.w._get_infos_on_page() == result

    def test_search_wikipedia(self):
        result = {'title': constants.WIKIPEDIA_INTRO["query"]["pages"]['332154']['title'],
                  'intro': constants.WIKIPEDIA_INTRO["query"]['pages']['332154']['extract']}
        assert self.w.search_wikipedia(lat=45.25653760000001, lng=5.0282228, sentence='connais palais idéal facteur cheval') == result
