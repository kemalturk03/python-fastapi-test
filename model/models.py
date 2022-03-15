from pydantic import BaseModel
from enum import Enum

class Gender(str,Enum):
    male: str="male"
    female: str="female"

class Student(BaseModel):
    id: int
    firstName: str
    lastName: str
    number: int
    gender: Gender
