import requests
from website.models import FrenchRegion, GrandPyQuery, init_db
import config

class TestStats:
    def setUp(self):
        init_db()

    def tearDown(self):
        pass

    def test_get_stats_nominal_case(self):
        response = requests.get(url='http://127.0.0.1:5000/stats/')
        print(response.json())
        assert len(response.json()) == 18
        assert response.status_code == 200

    def test_post_stats_nominal_case(self):
        
        initial_count = len(GrandPyQuery.query.all())
        
        payload={
            'sentence': 'connais tu le palais idéal du facteur cheval?'
        }
        response = requests.get(url='http://127.0.0.1:5000/AskGrandPy/', params=payload)
        # print(response.json())
        assert len(GrandPyQuery.query.all()) == initial_count + 1