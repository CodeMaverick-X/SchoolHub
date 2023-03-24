#!/usr/bin/python3
"""contains the class for events"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Event(BaseModel, Base):
    """the class for event"""

    __tablename__ = 'events'
    name = Column(String(128))
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    day = Column(String(128), nullable=True)
    time = Column(String(128), nullable=True)
    tag = Column(String(128), nullable=False)
    year = Column(Integer, nullable=True)
    semester = Column(Integer, nullable=True)


    def __init__(self, *args, **kwargs):
        """initializes events"""
        super().__init__(*args, **kwargs)
