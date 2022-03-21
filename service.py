from fastapi import FastAPI, Depends, HTTPException, status, Response
from database import engine
import database as db
import models
import schemas
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

@app.get("/get-all", status_code=status.HTTP_200_OK)
def getStudents(db: Session = Depends(db.get_db)):
    students = db.query(models.Student).all()
    return students


@app.get("/get-by-id/{id}", status_code=status.HTTP_200_OK)
def getById(id: int, response: Response, db: Session = Depends(db.get_db)):
    student = db.query(models.Student).filter(models.Student.id == id).first()
    if not student:
        response.status_code = status.HTTP_404_NOT_FOUND
        return HTTPException(status_code=404, detail=f"No student found with id {id}")
    return student


@app.post("/create-student", status_code=status.HTTP_200_OK)
def createStudent(request: schemas.Student, db: Session = Depends(db.get_db)):
    new_student = models.Student(
        firstName=request.firstName, lastName=request.lastName, number=request.number)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


@app.put("/update-student/{id}", status_code=status.HTTP_200_OK,response_model= schemas.UpdateStudent)
def updateStudent(id: int, request: schemas.Student, db: Session = Depends(db.get_db)):
    student = db.query(models.Student).filter(models.Student.id == id)

    if not student.first():
        return HTTPException(status_code=404, detail=f"No student found with id {id}")

    updatedStudent = {
        "firstName": request.firstName,
        "lastName": request.lastName,
        "number": request.number,
    }
    student.update(updatedStudent,synchronize_session=False)
    db.commit()

    return student.first()


@app.delete("/delete-student/{id}", status_code=status.HTTP_200_OK)
async def deleteStudent(id: int, db: Session = Depends(db.get_db)):
    student = db.query(models.Student).filter(models.Student.id == id)
    if not student.first():
        return HTTPException(status_code=404, detail=f"No student found with id {id}")
    student.delete(synchronize_session=False)
    db.commit()
    return {"Student Deleted"}