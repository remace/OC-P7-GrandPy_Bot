import requests


class Wikipedia_API:
    def __init__(self):
        self.url = 'https://fr.wikipedia.org/w/api.php'
        self.params = {}
        self.response = None

    def get_pages_around_location(self, lat, lng):
        self.params={
            "action": 'query',
            'list': 'geosearch',
            'format': 'json',
            'gsradius': 1000,
            'gslimit': 10,
            'gscoord': f"{lat}|{lng}"
        }
        self.response = requests.get(self.url, self.params).json()
        return self.response