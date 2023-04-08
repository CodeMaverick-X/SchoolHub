#!/usr/bin/python3
"""__courses.py__
    Desc: APIs for courses and also the route to set
    the current year and semester in the session
"""

from flask import Flask, session, request, g, jsonify, make_response
import models
from models.user import User
from models.course import Course
import os
from web_dynamic.api import api_views


@api_views.route('/courses', strict_slashes=False, methods=['GET'])
def get_courses():
    """view function to get users courses"""
    if not g.username:
        return make_response(jsonify({'error': 'invalid details user not in session'}), 400)

    user_id = g.user_id
    try:
        semester = int(g.semester)
        year = int(g.year)
    except(Exception):
        return make_response(jsonify({'error': 'invalid details'}), 400)

    if user_id and semester and year:
        courses = models.storage.get(User, user_id).courses
        c_list = [course.to_dict() for course in courses
                  if course.semester == semester 
                  and course.year == year]

        return make_response(jsonify(c_list), 200)
    return make_response(jsonify({'error': 'invalid details'}), 400)


@api_views.route('/courses', strict_slashes=False, methods=['POST'])
def create_courses():
    """view function to create users courses"""
    if not g.username:
        return make_response(jsonify({'error': 'invalid details user not in session'}), 400)

    user_id = g.user_id
    semester = g.semester
    year = g.year

    name = request.form['name']
    description = request.form['description']
    if name and user_id:
        course_info = {'user_id': user_id, 'name': name,
                       'description': description,
                       'semester': semester, 'year': year}
        course = Course(**course_info)
        course.save()
        course.create_grade()
        return make_response(jsonify(course.to_dict()), 201)
    else:
        return make_response(jsonify({'error': 'invalid details'}), 400)


@api_views.route('/set', strict_slashes=False, methods=['PUT'])
def set_default_sch_info():
    """set the default semester and year to display"""
    if not g.username:
        return make_response(jsonify({'error': 'invalid details'}), 400)

    user_id = g.user_id
    print('debug 1')
    user = models.storage.get(User, user_id)

    if not user:
        abort(400, description="Not a User")
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    yr = data.get('year')
    sm = data.get('semester')
    if not yr in range(1,6) or not sm in range(1, 3):
        return make_response(jsonify({'error': f'invalid details yr:{yr} sm:{sm}'}), 400)

    session['year'] = user.current_year = yr
    session['semester'] = user.current_semester = sm

    models.storage.save()
    user_dict = user.to_dict()
    current_details = {'year': user_dict['current_year'],
                       'semester': user_dict['current_semester']}
    return make_response(jsonify(current_details), 200)


@api_views.route('/set', strict_slashes=False, methods=['GET'])
def get_default_sch_info():
    """get the current selected school info"""
    if not g.username:
        return make_response(jsonify({'error': 'invalid details'}), 400)

    user_id = g.user_id
    username = g.username
    semester = g.semester
    year = g.year
    
    if user_id and semester and year and username:
        info_dict = {'user_id': user_id, 'semester': semester,
                     'year': year, 'username': username}
        return make_response(jsonify(info_dict), 200)
    return make_response(jsonify({}), 200)


@api_views.route('/courses/<course_id>',
                 strict_slashes=False, methods=['DELETE'])
def delete_course(course_id=None):
    """delete course based on id"""
    if not g.username:
        return make_response(jsonify({'error': 'invalid details'}), 400)

    user_id = g.user_id
    course = models.storage.get(Course, course_id)

    if course and course.user_id == user_id:
        models.storage.delete(course)
        models.storage.save()
        return make_response(jsonify({}), 200)
    return make_response(jsonify({}), 400)


@api_views.before_request
def load_user():
    g.username = None

    if 'user' in session:
        g.username = session.get('user')
        g.user_id = session.get('user_id')
        g.year = session.get('year')
        g.semester = session.get('semester')
