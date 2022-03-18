from sqlalchemy import Column,Integer,String
from enum import Enum
from database import Base 

class Gender(str,Enum):
    male: str="male"
    female: str="female"

class Student(Base):
    __tablename__ = "students"
    
    id= Column(Integer,primary_key=True,index=True)
    firstName= Column(Integer)
    lastName= Column(String)
    number= Column(Integer)