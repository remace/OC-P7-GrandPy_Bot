import config
import requests


class GMapsAPI:
    def __init__(self):
        self.params = {}
        self.api_url = "https://maps.googleapis.com/maps/api/geocode/json?"
        self.params['key'] = config.GOOGLE_MAPS_KEY

    def get_location(self, sentence):
        self.params['address'] = sentence
        return requests.get(self.api_url, params=self.params).json()

if __name__ == '__main__':
    gm = GMapsAPI()
    print(gm.get_location("connais palais idéal facteur cheval"))
