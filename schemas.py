from typing import Optional
from pydantic import BaseModel

class Student(BaseModel):
    firstName: str
    lastName: str
    number: int

class UpdateStudent(BaseModel):
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    number: Optional[int] = None