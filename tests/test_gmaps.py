from API import GMapsAPI
from unittest import TestCase
import urllib.request
from io import BytesIO
import json
from unittest import TestCase


class Test_GMapsAPI(TestCase):

    def setup_method(self):
        self.gm = GMapsAPI.GMapsAPI()

    def teardown_method(self):
        self.gm = None

    def test_http_result(self, monkeypatch):
        results = [{
            {"results":
                [{"address_components":
                      [{"long_name": "Palais Idéal",
                        "short_name": "Palais Idéal",
                        "types": ["establishment",
                                  "museum",
                                  "park",
                                  "point_of_interest"]},
                       {"long_name": "8", "short_name": "8", "types": ["street_number"]},
                       {"long_name": "Rue du Palais", "short_name": "Rue du Palais",
                        "types": ["route"]},
                       {"long_name": "Hauterives", "short_name": "Hauterives",
                        "types": ["locality", "political"]},
                       {"long_name": "Drôme",
                        "short_name": "Drôme",
                        "types": ["administrative_area_level_2",
                                  "political"]},
                       {"long_name": "Auvergne-Rhône-Alpes",
                        "short_name": "Auvergne-Rhône-Alpes",
                        "types": ["administrative_area_level_1", "political"]},
                       {"long_name": "France",
                        "short_name": "FR",
                        "types": ["country",
                                  "political"]},
                       {"long_name": "26390",
                        "short_name": "26390",
                        "types": ["postal_code"]}],
                  "formatted_address": "Palais Idéal, 8 Rue du Palais, 26390 Hauterives, France",
                  "geometry": {"location": {"lat": 45.25653760000001, "lng": 5.0282228},
                               "location_type": "ROOFTOP",
                               "viewport": {"northeast": {"lat": 45.25788658029151,
                                                          "lng": 5.029571780291502},
                                            "southwest": {"lat": 45.25518861970851,
                                                          "lng": 5.026873819708498}}},
                  "place_id": "ChIJjSFeXbA29UcRKXyFtaB1jcM",
                  "plus_code": {"compound_code": "724H+J7 Hauterives, France",
                                "global_code": "8FQ7724H+J7"},
                  "types": ["establishment",
                            "museum",
                            "park",
                            "point_of_interest"]}],
             "status": "OK"}
        }]

        def mock_return():
            return BytesIO(json.dumps(results).encode())

        monkeypatch.setattr(urllib.request, 'urlopen', mock_return)

        assert TestCase().assertDictEqual(self.gm.getlocation("connais facteur cheval"), results)
