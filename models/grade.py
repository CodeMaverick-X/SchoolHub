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
    weight = Column(Integer, nullable=True, default=0)
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
        """__calc_grade__
            Desc: assings a grade(alphabet) for a grade(instance of grade class),
            that is like A or B
            Desc: only calculates grade if the total score is more than 30 #update
        """
        t = self.total
        try:
            t = int(t)
        except(Exception):
            self.grade = "NA"
            return

        if t in range(1, 40):
            self.grade = "F"
        elif t in range(40, 45):
            self.grade = "E"
        elif t in range(45, 50):
            self.grade = "D"
        elif t in range(50, 60):
            self.grade = "C"
        elif t in range(60, 70):
            self.grade = "B"
        elif t in range(70, 101):
            self.grade = "A"
        else:
            self.grade = "NA"

