# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session, joinedload
from app.models.student_model import StudentModel
from fastapi import HTTPException
from app.schemas.student_schema import StudentCreateDTO
from sqlalchemy.exc import SQLAlchemyError

def get_all_student(db: Session, offset: int, limit: int):
    # Chưa tối ưu
    # return db.query(StudentModel).all()

    return db.query(StudentModel).options(joinedload(StudentModel.department)).offset(offset).limit(limit).all()

# Lấy sinh viên theo id
def get_student(db: Session, student_id: int):
    result = db.query(StudentModel).options(joinedload(StudentModel.department)).filter(StudentModel.id == student_id).first()
    if result is None:
        raise HTTPException(status_code=404, detail="Khong tim thay sinh vien")
    return result

# Thêm sinh viên
def create_student(db: Session, student: StudentCreateDTO):
    try:
        new_student = StudentModel(
            name = student.name,
            age = student.age,
            department_id = student.department_id
        )
        db.add(new_student)
        db.commit()
        db.refresh(new_student)

        return new_student
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Khong xac dinh")
