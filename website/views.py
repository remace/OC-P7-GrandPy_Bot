#!/usr/bin/env python3
"""
@desc website
@author Rémi "remace" Tauvel
@version 0.0.1
@date 2021-07-14
"""

from flask import Flask, render_template, request
import config

app = Flask(__name__)
app.config.from_object("config")


from libs.GrandPy import GrandPy
from .models import db, GrandPyQuery, FrenchRegion
from sqlalchemy import func


@app.route("/")
def index():
    return render_template("index.html", google_api_key=config.GOOGLE_MAPS_KEY)


@app.route("/AskGrandPy/", methods=["GET"])
def ask_grandpy():
    sentence = request.args.get("sentence")
    grandpy = GrandPy.GrandPy()
    return grandpy.answer(sentence)


@app.route("/stats/", methods=["GET", "POST"])
def stats():
    """either registers a new query in database if request is POST
    or gets every region's query count in database
    """
    if request.method == "POST":
        # region_name = request.args.get("region")
        # print(f"region_name: {region_name}")
        # region = FrenchRegion.query.filter(FrenchRegion.name == region_name)
        # print(f"region: {region}")
        # gpQuery = GrandPyQuery(region.id)
        # print(f"gpQuery: {gpQuery}")
        # db.session.add(gpQuery)
        # db.session.commit()
        return "hello post"

    if request.method == "GET":
        # get number of requests for every region
        query_numbers_by_region_as_tuple = (
            FrenchRegion.query.with_entities(
                FrenchRegion.name, func.count(GrandPyQuery.search_datetime)
            )
            .join(GrandPyQuery, GrandPyQuery.region_id == FrenchRegion.id, isouter=True)
            .group_by(FrenchRegion.name)
            .all()
        )

        # make it a dict
        query_number = {}
        for number in query_numbers_by_region_as_tuple:
            query_number[number[0]] = number[1]

        return query_number
