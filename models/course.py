#!/usr/bin/python3
"""contains the class for courses"""

import models
from models.base_model import BaseModel, Base
from models.grade import Grade
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Course(BaseModel, Base):
    """the class for course"""

    __tablename__ = 'courses'
    name = Column(String(60), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    description = Column(String(128), nullable=True)
    semester = Column(Integer, nullable=True)
    year = Column(Integer, nullable=True)
    grade = relationship("Grade", backref="course", uselist=False, cascade="all, delete, delete-orphan")


    def __init__(self, *args, **kwargs):
        """initializes courses"""
        super().__init__(*args, **kwargs)


    def create_grade(self):
        """__create_grade__
            Desc: create the grade for the course which has a one to one
            mapping to its course
        """
        grade_info = {'user_id': self.user_id, 'course_id': self.id,
                      'name': self.name, 'semester': self.semester,
                      'year': self.year, 'ca': 0, 'weight': 0, 'exam': 0, 'total': 0, 'grade': 'NA'}
        grade = Grade(**grade_info)
        grade.save()
