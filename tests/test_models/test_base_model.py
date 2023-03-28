#!/usr/bin/python3
"""test module for the base model class"""

import unittest
from models.base_model import BaseModel

class Test_BaseModel(unittest.Testcase):
    """test suit for base model"""

    def test_instance(self):
        """tests if object is instance of base model"""
        model = BaseModel()
        self.assertEqual()
        model.__class__ = BaseMOdel

