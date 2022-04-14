import requests
from website.models import FrenchRegion, GrandPyQuery, init_db
from sqlalchemy import func
import config
from libs.API import statsAPI
from . import constants


class TestStats:
    def setUp(self):
        init_db()

    def tearDown(self):
        pass

    def test_get_stats_nominal_case(self):
        response = requests.get(url="http://127.0.0.1:5000/stats/")
        print(response.json())
        assert len(response.json()) == 18
        assert response.status_code == 200
