#!/usr/bin/python3
"""__quotes.py__
    Desc: api that gets random quotes from an external api
"""

from flask import Flask, session, request, g, jsonify, make_response
import models
from models.user import User
from models.course import Course
import os
from web_dynamic.api import api_views
import requests


@api_views.route('/quote', strict_slashes=False, methods=['GET'])
def get_quote():
    """return quote using `api-ningas.com`"""
    headers = {'X-Api-Key': 'sOoLzL76uYbtL+SKbeLE4Q==QvArVlU4BFDxBu8X', 'limit': '1'}

    x = requests.get('https://api.api-ninjas.com/v1/quotes?category=education', headers=headers)

    if x.status_code == 200:
        return x.text
    else:
        return make_response(jsonify({'error': 'api failed'}), 500)
