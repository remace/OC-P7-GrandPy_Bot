#!/usr/bin/env python3
"""
@desc wikipedia API wrapper
@author Rémi "remace" Tauvel
@version 0.0.1
@date 2021-07-14
"""

import requests


class Wikipedia_API:
    def __init__(self):
        self.url = "https://fr.wikipedia.org/w/api.php"
        self.params = {}
        self.response = {}
        self.best_page = {}

    def _get_pages_around_location(self, lat, lng):
        self.params = {
            "action": "query",
            "list": "geosearch",
            "format": "json",
            "gsradius": 1000,
            "gslimit": 10,
            "gscoord": f"{lat}|{lng}",
        }
<<<<<<< HEAD
        self.response = requests.get(self.url, self.params).json()
        return {'wikipedia_infos': self.response,
                'status': 'OK'}
=======
        self.response = requests.get(url=self.url, params=self.params).json()
        return {"wikipedia_infos": self.response, "status": "OK"}
>>>>>>> 23222cc (pep 8)

    @staticmethod
    def title_score(page, sentence):
        """
        gives a score to a page depending on how early its words happen in the user request.
        the lower the score, the better the page fits the request
        """
        score = 0
        for word in page["title"].split(" "):
            if word in sentence.split(" "):
                score += page["title"].split(" ").index(word) + 1
        return score

    def _select_best_page(self, sentence):
        sentence_as_list = sentence.split(" ")
        previous_count = 0
        best_titles = {}
        index = -1
        # get only the most attractive pages
        for page in self.response["query"]["geosearch"]:
            count = 0
            index += 1
            for word in sentence_as_list:
                if word in page["title"].lower():
                    count += 1
            if count > previous_count:
                best_titles = {
                    page["title"]: {
                        "score": self.title_score(page, sentence),
                        "index": index,
                    },
                }
                previous_count = count
            elif count == previous_count:
                best_titles[page["title"]] = {
                    "score": self.title_score(page, sentence),
                    "index": index,
                }
        # select the page with the highest score
        index = -1
        previous_score = 999
        for title in best_titles:
            if best_titles[title]["score"] < previous_score:
                index = best_titles[title]["index"]
                previous_score = best_titles[title]["index"]
        if previous_count != 0:
            self.best_page = self.response["query"]["geosearch"][index]
            return self.best_page
        else:
            return []

    def _get_infos_on_page(self):
        self.params = {
            "action": "query",
            "prop": "extracts",
            "format": "json",
            "exintro": "true",
            "explaintext": "true",
            "pageids": self.best_page["pageid"],
        }

        response = requests.get(self.url, self.params).json()
        infos = {
            "title": response["query"]["pages"][f'{self.best_page["pageid"]}']["title"],
            "intro": response["query"]["pages"][f'{self.best_page["pageid"]}'][
                "extract"
            ],
        }
        return infos

    def search_wikipedia(self, lat, lng, sentence):
        self._get_pages_around_location(lat=lat, lng=lng)
        self._select_best_page(sentence)
        if self.best_page:
            infos = self._get_infos_on_page()
            return {"wikipedia_infos": {"info": infos, "status": "OK"}}
        else:
            return {"wikipedia_infos": {"info": [], "status": "ZERO_RESULT"}}
