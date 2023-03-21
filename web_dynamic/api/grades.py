#!/usr/bin/python3
"""restful api for grades and also the route to set the current year and semester"""

from flask import Flask, session, request, g, jsonify, make_response

import models
from models.user import User
from models.course import Course
from models.grade import Grade
import os
from web_dynamic.api import api_views


@api_views.route('/grades', strict_slashes=False, methods=['GET'])
def get_grades():
    """route to get grades"""
    user_id = session.get('user_id')
    semester = int(session.get('semester'))
    year = int(session.get('year'))

    if user_id and semester and year:
        grades = models.storage.all(Grade)
        g_list = [grade.to_dict() for grade in grades.values()\
                if grade.user_id == user_id and\
                grade.semester == semester and grade.year == year]

        return make_response(jsonify(g_list), 200)
    return make_response(jsonify({'error': 'invalid details'}), 400)


@api_views.route('/grades/<grade_id>', strict_slashes=False, methods=['PUT'])
def update_grades(grade_id=None):
    """update grades """

    grade = models.storage.get(Grade, grade_id)

    if grade:
        weight, ca, exam  = request.form['weight'], request.form['ca'], request.form['exam']

        if weight:
            grade.weight = int(weight)
        if ca:
            grade.ca = int(ca)
        if exam:
            grade.exam = int(exam)

        grade.total = grade.ca + grade.exam
        grade.calc_grade()
        models.storage.save()

        return make_response(jsonify({'success': True}), 200)
    return make_response(jsonify({'error': 'invalid details'}), 400)

