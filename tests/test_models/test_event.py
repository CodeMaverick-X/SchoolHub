#!/usr/bin/python3
"""tests for event class"""

import unittest
from models.user import User
from models.event import Event


class TestEvent(unittest.TestCase):
    """test cases for event"""

    def test_instance(self):
        """test if event is instance of Event"""
        user_info = {'password': 'my_password', 'username': 'test_user1'}
        user_in = User(**user_info)
        user_in.save()
        user_in.create_events()

        events = user_in.events
        len_of_ev = len(events)
        self.assertEqual(len_of_ev, 35)
        self.assertIs(type(events[0]), Event)
        self.assertNotEqual(events, [])
