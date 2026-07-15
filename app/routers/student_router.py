from fastapi import APIRouter, Depends
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session
from database import get_db
# from app.services.student_service import get_all_student
import app.services.student_service as student_service

student_router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

# Được phép tạo thêm nhiều router

#  API để get students
@student_router.get("/")
def get_all_student(offset: int = 0, limit: int = 3, db: Session = Depends(get_db)):
    return student_service.get_all_student(db, offset, limit)
