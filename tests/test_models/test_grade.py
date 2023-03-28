#!/usr/bin/python3
"""tests for grade class"""
import unittest
from models.grade import Grade
from models.user import User
from models.course import Course


class TestGrade(unittest.TestCase):
    """tests for grade"""

    def test_instance(self):
        """test if default values are created with grade object"""

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
        self.assertEqual(grade.ca, 0)
        self.assertEqual(grade.weight, 0)
        self.assertEqual(grade.exam, 0)
        self.assertEqual(grade.user_id, user_id)
        self.assertEqual(grade.course_id, c_i.id)

