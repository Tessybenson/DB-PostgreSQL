#!/usr/bin/env python3
""" Model for the store_records table """
from sqlalchemy import Column, Integer, String

from db.base_class import Base

class newStudentpy(Base):
    id = Column(Integer, primary_key=True, index=True)
    grade = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    def __str__(self):
        # Return a user-friendly string representation of the object
        return f"{self.id}, {self.grade}, {self.age}"
    
class oldStudentpy(Base):
    id = Column(Integer, primary_key=True, index=True)
    grade = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    def __str__(self):
        # Return a user-friendly string representation of the object
        return f"{self.id}, {self.grade}, {self.age}"