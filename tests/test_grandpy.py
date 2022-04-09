from tests import constants
from libs.GrandPy import GrandPy
import requests
import json


def mocked_requests_get(json_data,status_code):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data
    return MockResponse(json_data, status_code)

class Test_Grandpy:

  
    def setup_method(self):
        self.gp = GrandPy.GrandPy()


    def teardown_method(self):
        self.gp = None


    def test_answer(self, monkeypatch):
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

        def mock_return(*args, **kwargs):
            results_gmaps_api = constants.GMAPS_ANSWER
            results_wikipedia_API_gs = constants.JSON_WIKIPEDIA_RESPONSE_GEOSEARCH
            results_wikipedia_API_ext = constants.WIKIPEDIA_INTRO 
            if kwargs['url'] == 'https://fr.wikipedia.org/w/api.php':
                if kwargs['params'].get('list') == 'geosearch':
                    response = mocked_requests_get(json_data=results_wikipedia_API_gs, status_code=200)
                elif kwargs['params'].get('prop') == 'extracts':
                    response = mocked_requests_get(json_data=results_wikipedia_API_ext, status_code=200)
            elif kwargs['url'] == 'https://maps.googleapis.com/maps/api/geocode/json?':
                response = mocked_requests_get(json_data=results_gmaps_api, status_code=200)
            return response

        monkeypatch.setattr(requests, 'get', mock_return)
        assert self.gp.answer("connais-tu le palais idéal du facteur cheval?") == result


    def test_answer_maps_fails(self, monkeypatch):
        result = {
            'status': 'ZERO_RESULTS_GMAPS',
            'message': "je ne connais pas cet endroit. peut-être tu peux essayer d'être plus précis?"
        }
        def mock_return(*args, **kwargs):
            results_gmaps_api = constants.GMAPS_ANSWER_ZERO_RESULT
            response = mocked_requests_get(json_data=results_gmaps_api, status_code=200)
            return response

        monkeypatch.setattr(requests, 'get', mock_return)

        assert self.gp.answer("oeurtgbq^ùoqebngf ùqerdg n") == result

    def test_answer_wikipedia_fails(self, monkeypatch):
        result = {
            'status': 'ZERO_RESULTS_WIKI',
            'maps_info': constants.USEFUL_DATA_LAUBRE,
            'message': "j'ai l'impression que c'est là. essaye de me dire dans quelle ville ça se trouve dans ta question"
        }

        def mock_return(*args, **kwargs):
            results_gmaps_api = constants.GMAPS_ANSWER_LAUBRE
            results_wikipedia_API_gs = constants.JSON_WIKIPEDIA_RESPONSE_GEOSEARCH_VOID
            if kwargs['url'] == 'https://fr.wikipedia.org/w/api.php':
                response = mocked_requests_get(json_data=results_wikipedia_API_gs, status_code=200)
            elif kwargs['url'] == 'https://maps.googleapis.com/maps/api/geocode/json?':
                response = mocked_requests_get(json_data=results_gmaps_api, status_code=200)
            return response

        monkeypatch.setattr(requests, 'get', mock_return)
        
        assert self.gp.answer("Rue de Laubre 07400 meysse") == result