from API import wikipedia_API, GMapsAPI
from parsing import parser


class GrandPy:

    def __init__(self):
        self.parser = parser.SentenceParser()
        self.google_maps = GMapsAPI.GMapsAPI()
        self.wikipedia = wikipedia_API.Wikipedia_API()

    def answer(self, sentence):
        response={}
        clean_sentence = self.parser.get_clean_sentence(sentence)
        response['maps_info'] = self.google_maps.search(clean_sentence)
        response['wiki_info'] = self.wikipedia.search_wikipedia(response['maps_info']['results']['geometry']['location']['lat'],
                                                                response['maps_info']['results']['geometry']['location']['lng'],
                                                                clean_sentence)
        return response
