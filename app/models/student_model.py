from sqlalchemy import Column, String, Integer, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class StudentModel(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)

    # Liên kết theo mối quan hệ 1 - 1
    # Liên kết mối quan hệ theo chiêu xuôi
    profile = relationship("ProfileModel", back_populates="student", uselist=False)


class ProfileModel(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    bio = Column(String(100))
    #  Tạo khóa ngoại
    student_id = Column(Integer, ForeignKey("students.id"), unique=True)
    # Liên kết theo chiều ngược
    student = relationship("StudentModel", back_populates="profile")

# Tạo bảng Department liên kết với bảng student với mối quan hệ 1 nhiều
# Tạo bảng course liên kết với bảng student với mối quan hệ nhiều nhiều