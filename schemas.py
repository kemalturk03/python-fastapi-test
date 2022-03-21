#schemas file is for storing BaseModel models.

from pydantic import BaseModel, Field
from enum import Enum

class Gender(str,Enum):
    male: str="male"
    female: str="female"

class Student(BaseModel):
    firstName: str
    lastName: str
    number: int

class UpdateStudent(Student):
    class Config():
        orm_mode = True