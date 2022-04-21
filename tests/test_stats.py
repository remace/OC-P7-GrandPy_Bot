import requests
from website import app
from website.models import FrenchRegion, GrandPyQuery, init_db
from libs.API import statsAPI

from . import constants
import config_test

app.config.from_object("config_test")

class TestStats():
    
    def setUp(self):
        init_db()
        print("database initialized")    

    def tearDown(self):
        pass

    def test_new_grandpy_request(self):
        self.setUp()
        gpq = GrandPyQuery(1)
        assert gpq.region_id == 1

    def test_get_stats_nominal_case(self):
        self.setUp()
        with app.test_client() as test_client:
            response = test_client.get("http://127.0.0.1:5000/stats/")
            assert len(response.json) == 18
            assert response.status_code == 200
