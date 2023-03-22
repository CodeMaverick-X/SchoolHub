#!/usr/bin/python3
"""contains the class for grades"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Grade(BaseModel, Base):
    """the class for grade"""

    __tablename__ = 'grades'
    course_id = Column(String(60), ForeignKey('courses.id'), nullable=False)
    name = Column(String(60), nullable=True)
    user_id = Column(String(60), nullable=False)
    weight = Column(Integer, nullable=True)
    ca = Column(Integer, nullable=True)
    exam = Column(Integer, nullable=True)
    total = Column(Integer, nullable=True)
    semester = Column(Integer, nullable=True)
    year = Column(Integer, nullable=True)
    grade = Column(String(24), nullable=True)
    
    
    def __init__(self, *args, **kwargs):
        """initializes grade"""
        super().__init__(*args, **kwargs)


    def calc_grade(self):
        """assings a grade for a grade, that is like A or B
            Desc: only calculates grade if the total score is more than 30
        """
        t = self.total
        if (t >= 40 and t < 45):
            self.grade = "E"
        elif (t >= 45 and t < 50):
            self.grade = "D"
        elif (t >= 50 and t < 60):
            self.grade = "C"
        elif (t >= 60 and t < 70):
            self.grade = "B"
        elif (t >= 70 and t <= 100):
            self.grade = "A"
        else:
            self.grade = "NA"

