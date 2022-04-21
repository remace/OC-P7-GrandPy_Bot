from website import app
from website.models import init_db

class TestIndex:
    def setUp(self):
        init_db()
        pass

    def tearDown(self):
        pass

    def test_index_get(self):
        self.setUp()
        with app.test_client() as test_client:
            response = test_client.get("/")
            assert response.status_code == 200

    def test_grandpy_response_get(self):
        self.setUp()
        with app.test_client() as test_client:
            response = test_client.get("/AskGrandPy/?sentence=Paris")
            assert response.status_code == 200