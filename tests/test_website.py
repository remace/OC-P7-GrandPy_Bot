from website import app


class TestIndex:
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_index_get(self):
        with app.test_client() as test_client:
            response = test_client.get("/")
            assert response.status_code == 200

    def test_grandpy_response_get(self):
        with app.test_client() as test_client:
            response = test_client.get("/AskGrandPy/?sentence=Washington")
            assert response.status_code == 200