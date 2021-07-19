import config
import requests


class GMapsAPI:
    def __init__(self):
        self.req = {}
        self.api_url = "https://maps.googleapis.com/maps/api/geocode/json"
        self.req['api_key'] = config.GOOGLE_MAPS_KEY

    def get_location(self, sentence):
        self.req['address'] = sentence
        return requests.post(self.api_url, data=self.req)
