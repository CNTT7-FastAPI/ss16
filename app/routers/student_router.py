from fastapi import APIRouter, Depends
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session
from database import get_db
# from app.services.student_service import get_all_student
import app.services.student_service as student_service
from app.schemas.student_schema import StudentResponse, StudentCreateDTO

student_router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

# Được phép tạo thêm nhiều router

#  API để get students
@student_router.get("/", response_model=list[StudentResponse])
def get_all_student(offset: int = 0, limit: int = 3, db: Session = Depends(get_db)):
    return student_service.get_all_student(db, offset, limit)
    
# API get 1 sinh viên
@student_router.get("/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    return student_service.get_student(db, student_id)


# API thêm 1 sinh viên
@student_router.post("/", response_model=StudentResponse)
def create_student(student: StudentCreateDTO,db: Session = Depends(get_db)):
    return student_service.create_student(db, student)