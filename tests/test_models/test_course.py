#!/usr/bin/python3
"""test for courses"""

import unittest
from models.course import Course
from models.user import User
from models.grade import Grade
from models.base_model import BaseModel


class TestCourses(unittest.TestCase):
    """test for courses"""
    def test_instance(self):
        """test if course is an instance of Course"""

        user_info = {'username':'test_user', 'password': 'super_secrete'}

        user = User(**user_info)
        user.save()
        user_id = user.id

        course_info = {'user_id': user_id, 'name': 'test_course'}

        c_i = Course(**course_info)
        c_i.save()
        self.assertEqual(c_i.user_id, user_id)
        self.assertIs(type(c_i), Course)
        self.assertIsInstance(c_i, BaseModel)


    def test_create_grade(self):
        """test the create grade method"""

        user_info = {'username':'test_user', 'password': 'super_secrete'}

        user = User(**user_info)
        user.save()
        user_id = user.id

        course_info = {'user_id': user_id, 'name': 'test_course'}

        c_i = Course(**course_info)
        c_i.save()

        c_i.create_grade()
        grade = c_i.grade

        self.assertIs(type(grade), Grade)

