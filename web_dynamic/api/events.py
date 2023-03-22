#!/usr/bin/python3
"""restful api for events"""

from flask import Flask, session, request, g, jsonify, make_response

import models
from models.user import User
from models.course import Course
from models.grade import Grade
from models.event import Event
import os
from web_dynamic.api import api_views


@api_views.route('/events', strict_slashes=False, methods=['GET'])
def get_events():
    """get all events for a specific user"""
    user_id = session.get('user_id')

    user = models.storage.get(User, user_id)

    events = [event.to_dict() for event in user.events]

    return make_response(jsonify(events), 200)


@api_views.route('/events', strict_slashes=False, methods=['PUT'])
def edit_events():

    name = request.form['name']
    tag = request.form['tag']
    user_id = session.get('user_id')
    user = models.storage.get(User, user_id)

    if user and name and tag:
        events = user.events
        for event in events:
            if event.tag == tag:
                event.name = name
        models.storage.save()
        return make_response(jsonify({'success': True}), 200)
    return make_response(jsonify({'success': False}), 400)


