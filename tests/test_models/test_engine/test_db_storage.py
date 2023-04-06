#!/usr/bin/python3
"""test the database class"""

from models import storage
from models.user import User
from models.event import Event
from models.engine.db_storage import DBStorage
import unittest


class TestDatabase(unittest.TestCase):
    """test the database"""

    def test_instance(self):
        """test storage is instance of DBStorage"""

        self.assertIs(type(storage), DBStorage)

    def test_get(self):
        """test thet get method in dbstorage"""

        user_info = {'username': 'test_username', 'password': 'super_secrete'}

        user = User(**user_info)
        user.save()

        same_user = storage.get(User, user.id)

        self.assertIs(same_user, user)

    def test_count(self):
        """test cont method"""

        user_info = {'username': 'test_username', 'password': 'super_secrete'}

        user = User(**user_info)
        user.save()
        user.create_events()

        all_class_count = storage.count()
        self.assertEqual(all_class_count, 152) # 36 from the events, 3 users from the total test, 1 course, 1 grade

        user_count = storage.count(User)
        self.assertEqual(user_count, 7)


    def tearDown(self):
        """tear down database"""
        pass
        

