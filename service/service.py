from fastapi import HTTPException, Path
from fastapi import FastAPI
from sample_data import students

app = FastAPI()
apiBaseUrl = "/api/v1"


@app.get(f"{apiBaseUrl}")
def getStudents():
    return students

@app.delete(f"{apiBaseUrl}/delete-student/"+ "{id}")
async def deleteStudent(id:int=Path(None,description="ID to be deleted")):
    for student in students:
        if student.id == id:
            students.remove(student)
            return students
    return HTTPException(status_code=404,detail=f"Student ID with {id} not found")        