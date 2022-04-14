import requests
from website.models import db, GrandPyQuery, FrenchRegion
from sqlalchemy import func


class StatsAPI:
    def __init__(self):
        self.maps_data = {}

    def set_maps_data(self, maps_data):
        self.maps_data = maps_data

    def register_query(self):
        address_components = self.maps_data["results"]["address_components"]
        for comp in address_components:
            if comp["types"][0] == "country" and comp["long_name"] == "France":
                for component in address_components:
                    if component["types"][0] == "administrative_area_level_1":
                        region = FrenchRegion.query.filter(
                            FrenchRegion.name == component["long_name"]
                        ).all()[0]
                        grandpy_query = GrandPyQuery(region.id)
                        db.session.add(grandpy_query)
                        db.session.commit()
