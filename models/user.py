#!/usr/bin/python3
""" holds class User"""

import models
from models.base_model import BaseModel, Base
from models.event import Event
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """user class"""


    __tablename__ = 'users'
    password = Column(String(128), nullable=False)
    username = Column(String(128), nullable=True)
    current_semester = Column(Integer, nullable=True)
    current_year = Column(Integer, nullable=True)
    courses = relationship("Course", backref="user", cascade="all, delete, delete-orphan")
    events = relationship("Event", backref="user", cascade="all, delete, delete-orphan")

    
    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)


    def create_events(self):
        """__create_events__
            Desc: cerates the event slots, the user only gets to edit the events not create
            then.
        """
        days = {"MON": "monday", "TUE": "tuesday", "WED": "wednesday", "THU": "thursday",
                "FRI": "friday", "SAT": "saturday", "SUN": "sunday"}
        times = ["8-10", "10-12", "12-14", "14-16", "16-18"]

        for day in days.keys():
            for time in times:
                tag = day+"_"+time
                info = {"tag": tag, "user_id": self.id, "day": day, "time": time, "name": "",
                        "day": days[day], "time": time}

                ev = Event(**info)
                ev.save()
