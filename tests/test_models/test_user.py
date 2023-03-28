#!/usr/bin/python3
"""test suite for user"""

import unittest
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    """start"""

    def test_instance_user(self):
        """test  instance of user"""
        user_info = {'password': 'my_password', 'username': 'test_user'}
        user_in = User(**user_info)
        self.assertIs(type(user_in), User)
        self.assertEqual(user_in.password, 'my_password')

    def test_subclass(self):
        """test if subclass of basemodel"""

        user_info = {'password': 'my_password', 'username': 'test_user'}
        user_in = User(**user_info)

        self.assertIsInstance(user_in, BaseModel)

    def test_create_events(self):
        """test if events are created for user"""
        user_info = {'password': 'my_password', 'username': 'test_user1'}
        user_in = User(**user_info)
        user_in.save()
        user_in.create_events()

        events = user_in.events
        self.assertNotEqual(events, [])
