#!/usr/bin/python3
""" Blueprint for pages """
from flask import Blueprint

page_views = Blueprint('page_views', __name__, template_folder='templates', static_folder='statics')


from web_dynamic.pages.pages import *
