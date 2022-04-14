from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from .views import app

db = SQLAlchemy(app)


class FrenchRegion(db.Model):
    __tablename__ = "region"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    queries = db.relationship("GrandPyQuery", backref="region", lazy=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"[{self.id}: {self.name}]"


class GrandPyQuery(db.Model):
    __tablename__ = "query"
    id = db.Column(db.Integer, primary_key=True)
    search_datetime = db.Column(db.DateTime, nullable=False)
    region_id = db.Column(db.Integer, db.ForeignKey("region.id"), nullable=False)

    def __init__(self, region_id):
        self.search_datetime = datetime.now()
        self.region_id = region_id

        def __repr__(self):
            return f"{self.search_datetime}\t{self.region}"


def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(FrenchRegion("Auvergne-Rhône-Alpes"))
    db.session.add(FrenchRegion("Bourgogne-Franche-Comté"))
    db.session.add(FrenchRegion("Bretagne"))
    db.session.add(FrenchRegion("Centre-Val de Loire"))
    db.session.add(FrenchRegion("Corse"))
    db.session.add(FrenchRegion("Grand Est"))
    db.session.add(FrenchRegion("Hauts-de-France"))
    db.session.add(FrenchRegion("Île-de-France"))
    db.session.add(FrenchRegion("Normandie"))
    db.session.add(FrenchRegion("Nouvelle-Aquitaine"))
    db.session.add(FrenchRegion("Occitanie"))
    db.session.add(FrenchRegion("Pays de la Loire"))
    db.session.add(FrenchRegion("Provence-Alpes-Côte d'Azur"))
    db.session.add(FrenchRegion("Guadeloupe"))
    db.session.add(FrenchRegion("Martinique"))
    db.session.add(FrenchRegion("Guyane"))
    db.session.add(FrenchRegion("La Réunion"))
    db.session.add(FrenchRegion("Mayotte"))
    db.session.commit()
