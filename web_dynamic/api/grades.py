#!/usr/bin/python3
"""API for grade controller"""

from flask import Flask, session, request, g, jsonify, make_response
import models
from models.user import User
from models.course import Course
from models.grade import Grade
import os
from web_dynamic.api import api_views
from math import ceil


@api_views.route('/grades', strict_slashes=False, methods=['GET'])
def get_grades():
    """route to get grades"""
    if not g.username:
        return make_response(jsonify({'error': 'invalid details'}), 400)

    user_id = g.user_id
    try:
        semester = int(g.semester)
        year = int(g.year)
    except(Exception):
        return make_response(jsonify({'error': 'invalid info details or type'}), 400)

    user = models.storage.get(User, user_id)
    if user and semester and year:
        grades = [course.grade.to_dict() for course in user.courses
                  if course.semester == semester
                  and course.year == year]

        g_count = 0
        used_c = 0
        qp = 0
        for grade in grades:
            wt = grade['weight']

            if grade['grade'] == 'NA' or not wt:
                continue
            elif grade['grade'] == 'A':
                used_c += 1
                g_count += wt
                qp += 5 * wt
            elif grade['grade'] == 'B':
                used_c += 1
                g_count += wt
                qp += 4 * wt
            elif grade['grade'] == 'C':
                used_c += 1
                g_count += wt
                qp += 3 * wt
            elif grade['grade'] == 'D':
                used_c += 1
                g_count += wt
                qp += 2 * wt
            elif grade['grade'] == 'E':
                used_c += 1
                g_count += wt
                qp += 1 * wt
            elif grade['grade'] == 'F':
                used_c += 1
                g_count += wt
                qp += 0 * wt
        
        if g_count >= 1:
            gpa = qp / g_count
        else:
            gpa = 0
        grade_info = [round(gpa, 2), used_c, g_count]

        info = [grades, grade_info]


        return make_response(jsonify(info), 200)
    return make_response(jsonify({'error': 'invalid details'}), 400)


@api_views.route('/grades/<grade_id>', strict_slashes=False, methods=['PUT'])
def update_grades(grade_id=None):
    """update grades """
    if not g.username:
        return make_response(jsonify({'error': 'invalid details'}), 400)

    grade = models.storage.get(Grade, grade_id)
    user_id = g.user_id

    if grade and grade.user_id == user_id:
        weight, ca, exam = request.form['weight'],\
                            request.form['ca'], request.form['exam']

        try:
            if weight:
                grade.weight = int(weight)
            if ca:
                grade.ca = int(ca)
            if exam:
                grade.exam = int(exam)
        except(Exception):
            return make_response(jsonify({'error': 'invalid details'}), 400)
        
        if grade.ca and grade.exam:
            grade.total = grade.ca + grade.exam
        grade.calc_grade()
        models.storage.save()

        return make_response(jsonify({'success': True}), 200)
    return make_response(jsonify({'error': 'invalid details'}), 400)


@api_views.before_request
def load_user():
    g.username = None

    if 'user' in session:
        g.username = session.get('user')
        g.user_id = session.get('user_id')
        g.year = session.get('year')
        g.semester = session.get('semester')
