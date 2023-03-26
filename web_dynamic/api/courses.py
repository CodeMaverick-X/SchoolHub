#!/usr/bin/python3
"""restful api for courses and also the route to set the current year and semester"""

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
    semester = int(session.get('semester'))
    year = int(session.get('year'))

    if user_id and semester and year:
        courses = models.storage.all(Course)
        c_list = [course.to_dict() for course in courses.values()\
                if course.user_id == user_id\
                and course.semester == semester and course.year == year]

        return make_response(jsonify(c_list), 200)
    return make_response(jsonify({'error': 'invalid details'}), 400)


@api_views.route('/courses', strict_slashes=False, methods=['POST'])
def create_courses():
    """view function to create users courses"""
    user_id = session.get('user_id')
    semester = session.get('semester')
    year = session.get('year')

    name = request.form['name']
    description = request.form['description']
    if name and user_id:
        course_info = {'user_id': user_id, 'name': name, 'description': description, 'semester': semester, 'year': year}
        course = Course(**course_info)
        course.save()
        course.create_grade()
        return make_response(jsonify(course.to_dict()), 201)
    else:
        return make_response(jsonify({'error': 'invalid details'}), 400)


@api_views.route('/set', strict_slashes=False, methods=['PUT'])
def set_default_sch_info():
    """set the default info to display"""
    user_id = session.get('user_id')

    user = models.storage.get(User, user_id)

    if not user:
        abort(400, description="Not a User")

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    session['year'] = user.current_year = data.get('year')
    session['semester'] = user.current_semester = data.get('semester')

    models.storage.save()
    u_d = user.to_dict()
    current_details = {'year': u_d['current_year'], 'semester': u_d['current_semester']}
    return make_response(jsonify(current_details), 200)


@api_views.route('/set', strict_slashes=False, methods=['GET'])
def get_default_sch_info():
    """get the current selected school info"""
    user_id = session.get('user_id')
    semester = session.get('semester')
    year = session.get('year')
    username = models.storage.get(User, user_id).username

    if user_id and semester and year:

        info_dict = {'user_id': user_id, 'semester': semester, 'year': year, 'username': username}

        return make_response(jsonify(info_dict), 200)

    return make_response(jsonify({}), 200)


@api_views.route('/courses/<course_id>', strict_slashes=False, methods=['DELETE'])
def delete_course(course_id=None):
    """delete course based on id"""
    course = models.storage.get(Course, course_id)


    if course:
        models.storage.delete(course)
        models.storage.save()
        return make_response(jsonify({}), 200)
    return make_response(jsonify({}), 400)


