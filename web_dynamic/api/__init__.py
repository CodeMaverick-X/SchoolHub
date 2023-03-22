#!/usr/bin/python3
""" Blueprint for pages """
from flask import Blueprint

api_views = Blueprint('api_views', __name__, url_prefix='/api/v1')

from web_dynamic.api.courses import *
from web_dynamic.api.grades import *
from web_dynamic.api.events import *

