#!/usr/bin/env python3
"""
@desc website
@author Rémi "remace" Tauvel
@version 0.0.1
@date 2021-07-16
"""
GMAPS_ANSWER = {"results":
    [
        {"address_components":
             [{"long_name":
                   "Palais Idéal",
               "short_name":
                   "Palais Idéal",
               "types":
                   ["establishment", "museum", "park", "point_of_interest"]},
              {"long_name":
                   "8", "short_name":
                   "8",
               "types":
                   ["street_number"]},
              {"long_name":
                   "Rue du Palais",
               "short_name":
                   "Rue du Palais",
               "types":
                   ["route"]},
              {"long_name":
                   "Hauterives",
               "short_name":
                   "Hauterives",
               "types":
                   ["locality", "political"]},
              {"long_name":
                   "Drôme",
               "short_name":
                   "Drôme",
               "types":
                   ["administrative_area_level_2", "political"]},
              {"long_name":
                   "Auvergne-Rhône-Alpes",
               "short_name":
                   "Auvergne-Rhône-Alpes",
               "types":
                   ["administrative_area_level_1", "political"]},
              {"long_name":
                   "France",
               "short_name":
                   "FR",
               "types":
                   ["country", "political"]},
              {"long_name":
                   "26390",
               "short_name":
                   "26390",
               "types":
                   ["postal_code"]}],
         "formatted_address":
             "Palais Idéal, 8 Rue du Palais, 26390 Hauterives, France",
         "geometry":
             {"location":
                  {"lat":
                       45.25653760000001, "lng":
                       5.0282228},
              "location_type":
                  "ROOFTOP",
              "viewport":
                  {"northeast":
                       {"lat":
                            45.25788658029151,
                        "lng":
                            5.029571780291502},
                   "southwest":
                       {"lat":
                            45.25518861970851,
                        "lng":
                            5.026873819708498}
                   }
              },
         "place_id":
             "ChIJjSFeXbA29UcRKXyFtaB1jcM",
         "plus_code":
             {"compound_code":
                  "724H+J7 Hauterives, France",
              "global_code":
                  "8FQ7724H+J7"},
         "types":
             ["establishment", "museum", "park", "point_of_interest"]
         }],
    "status":
        "OK"}

GMAPS_ANSWER_ZERO_RESULT = {
    "results": [],
    "status": "ZERO_RESULTS"}

USEFUL_DATA = {"results":
    {
        'name':
            'Palais Idéal',
        'formatted_address':
            'Palais Idéal, 8 Rue du Palais, 26390 Hauterives, France',
        'geometry':
            {'location':
                 {'lat':
                      45.25653760000001,
                  'lng':
                      5.0282228
                  },
             "location_type":
                 "ROOFTOP",
             'viewport':
                 {
                     'northeast':
                         {"lat":
                              45.25788658029151,
                          'lng':
                              5.029571780291502
                          },
                     'southwest':
                         {"lat":
                              45.25518861970851,
                          "lng":
                              5.026873819708498
                          }
                 }
             }
    },
    'status': "OK"
}

USEFUL_DATA_LAUBRE = {'results': {
        'formatted_address': 'Rue de Laubre, 07400 Meysse, France',
        'geometry': {
            'bounds':{
                'northeast':
                    {'lat': 44.6173264,
                     'lng': 4.7219326
                     },
                'southwest':{
                    'lat': 44.61466069999999,
                    'lng': 4.7209626}
                    },
            'location': {'lat': 44.6160179,
                         'lng': 4.7216464},
            'location_type': 'GEOMETRIC_CENTER',
            'viewport': {
                'northeast': {
                    'lat': 44.61734253029149,
                    'lng': 4.722796580291503},
                'southwest': {'lat': 44.6146445697085,
                              'lng': 4.720098619708498}
               }
        },
        'name': 'Rue de Laubre'
    },
        'status': 'OK'
}

JSON_WIKIPEDIA_RESPONSE_GEOSEARCH = {'wikipedia_infos': {"batchcomplete": "",
                                                         "query":
                                                             {"geosearch":
                                                                 [{
                                                                     "pageid": 332154,
                                                                     "ns": 0,
                                                                     "title": "Palais idéal",
                                                                     "lat": 45.256267,
                                                                     "lon": 5.028506,
                                                                     "dist": 37.4,
                                                                     "primary": ""
                                                                 },
                                                                     {
                                                                         "pageid": 7966431,
                                                                         "ns": 0,
                                                                         "title": "Villa Alicius",
                                                                         "lat": 45.255889,
                                                                         "lon": 5.027794,
                                                                         "dist": 79.5,
                                                                         "primary": ""},
                                                                     {
                                                                         "pageid": 355220,
                                                                         "ns": 0,
                                                                         "title": "Hauterives",
                                                                         "lat": 45.2561111111,
                                                                         "lon": 5.02722222222,
                                                                         "dist": 91.6,
                                                                         "primary": ""},
                                                                     {
                                                                         "pageid": 7961734,
                                                                         "ns": 0,
                                                                         "title": "Château de Hauterives (Drôme)",
                                                                         "lat": 45.2539,
                                                                         "lon": 5.0293,
                                                                         "dist": 305.2,
                                                                         "primary": ""
                                                                     }]
                                                             }
                                                         },
                                     'status': 'OK'
                                     }

JSON_WIKIPEDIA_RESPONSE_GEOSEARCH_VOID = {
    "batchcomplete": "",
    "query": {
        "geosearch": []
    }
}

WIKIPEDIA_INTRO = {"batchcomplete": "",
                   "query": {
                       "pages":
                           {"332154":
                                {"pageid": 332154,
                                 "ns": 0,
                                 "title": "Palais idéal",
                                 "extract": "Le Palais idéal (aussi appelé le Palais idéal du facteur Cheval) est un "
                                            "monument construit à Hauterives (France) par le facteur Ferdinand Cheval, "
                                            "de 1879 à 1912.\nChef-d'œuvre de l'architecture naïve et de l'art naïf, "
                                            "il est classé au titre des monuments historiques depuis 1969.\nÀ "
                                            "l'occasion d'un vote organisé durant l'été 2020, au niveau national, "
                                            "par les producteurs de l'émission Le Monument préféré des Français, "
                                            "diffusée sur France Télévisions, le Palais idéal a été classé deuxième "
                                            "sur une liste de quatorze monuments. Sa construction a également fait "
                                            "l'objet d'un film biographique français réalisé par Nils Tavernier et "
                                            "sorti en 2018."}
                            }
                   }
                   }
