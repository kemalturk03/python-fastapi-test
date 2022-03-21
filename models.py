#models file is for storing sqlalchemy models or database models.

from sqlalchemy import Column,Integer,String
from database import Base 

class Student(Base):
    __tablename__ = "students"
    
    id= Column(Integer,primary_key=True,index=True)
    firstName= Column(Integer)
    lastName= Column(String)
    number= Column(Integer)