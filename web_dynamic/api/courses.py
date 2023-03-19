#!/usr/bin/python3
"""restful api for courses"""

from flask import Flask, session, request, g, jsonify, make_response

import models
from models.user import User
from models.course import Course
import os
from web_dynamic.api import api_views


@api_views.route('/courses', strict_slashes=False, methods=['GET'])
def get_courses():
    """view function to get users courses"""
    user_id = session.get('user_id')
    if user_id:
        courses = models.storage.all(Course)
        c_list = [course.to_dict() for course in courses.values() if course.user_id == user_id]

        return make_response(jsonify(c_list), 200)


@api_views.route('/courses', strict_slashes=False, methods=['POST'])
def create_courses():
    """view function to create users courses"""
    user_id = session.get('user_id')

    name = request.form['name']
    description = request.form['description']
    if name and user_id:
        course_info = {'user_id': user_id, 'name': name, 'description': description}
        course = Course(**course_info)
        course.save()
        return make_response(jsonify(course.to_dict()), 201)
    else:
        return make_response(jsonify({'error': 'invalid details'}), 400)


