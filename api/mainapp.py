#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lemmatizer-API

An API which lemmatizes Lithuanian text using tools developed by Semantika.lt

Creayed 2021 12 04
@author: lukasp
"""


import json
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

from lemmatizer import Lemmatizer, LEX, MORPH


# API CONFIG
app = Flask(__name__)
CORS(app)
api = Api(app)

# Initialise request parser; specify expected and required arguments
parser = reqparse.RequestParser()

parser.add_argument("text")

# Configure the display page running on "/"
file = open("index_html", "r")
hello_ht = file.read()
file.close()


@app.route("/")
def hello():
    """Loads Landing Page"""
    return hello_ht


class LemmatizerEndpoint(Resource):
    """
    Endpoint to submit lemmatization tasks
    """

    def __init__(self):
        self.LEX = LEX
        self.MORPH = MORPH

    def post(self):
        """
        Executes text lemmatization

        RETURNS:
            list of dicts
            {"original": original token, "lemma": lemmatized token, "morph": morphological annotation}
        """

        args = parser.parse_args()

        lem = Lemmatizer(self.LEX, self.MORPH)
        result = lem.lemmatize_text(args["text"])

        return result

api.add_resource(LemmatizerEndpoint, "/lemmatize")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

