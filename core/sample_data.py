from typing import List
from models import Gender,Student


students: List[Student]= [
    Student(
        id=1,
        firstName="Kemal",
        lastName="Türk",
        number=12345,
        gender=Gender.male
    ),
    Student(
        id=2,
        firstName="Ayşe",
        lastName="Türk",
        number=78945,
        gender=Gender.female
        )
]